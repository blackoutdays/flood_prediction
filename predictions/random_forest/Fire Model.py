import numpy as np
import cv2
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.efficientnet import preprocess_input
from tensorflow.keras import layers, Model
from tensorflow.keras.applications import EfficientNetB0

# Пути к данным
DATA_PATHS = {
    "train": {
        "Fire": Path("C:\\Users\\Alshr_Ardqly\\Downloads\\Data\\Train_Data\\Fire"),
        "NonFire": Path("C:\\Users\\Alshr_Ardqly\\Downloads\\Data\\Train_Data\\Non_Fire")
    },
    "test": {
        "Fire": Path("C:\\Users\\Alshr_Ardqly\\Downloads\\Data\\Test_Data\\Fire"),
        "NonFire": Path("C:\\Users\\Alshr_Ardqly\\Downloads\\Data\\Test_Data\\Non_Fire")
    }
}

# Константы
IMAGE_SIZE = (256, 256)
BATCH_SIZE = 32
LABELS = {"Fire": 0, "NonFire": 1}

def load_images_from_directory(directory_path, label, image_size):
    """Загрузка и обработка изображений."""
    images, labels = [], []
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
    for image_path in directory_path.glob("*"):
        if image_path.suffix.lower() in image_extensions:
            img = cv2.imread(str(image_path))
            if img is not None:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                img = cv2.resize(img, image_size)
                images.append(img)
                labels.append(label)
    return np.array(images), np.array(labels)

def prepare_dataset(data_paths, labels_dict, image_size):
    """Создание полного набора данных."""
    images, labels = [], []
    for label_name, label_path in data_paths.items():
        class_images, class_labels = load_images_from_directory(label_path, labels_dict[label_name], image_size)
        images.append(class_images)
        labels.append(class_labels)
    return np.concatenate(images), np.concatenate(labels)

# Загрузка данных
X_train, y_train = prepare_dataset(DATA_PATHS["train"], LABELS, IMAGE_SIZE)
X_test, y_test = prepare_dataset(DATA_PATHS["test"], LABELS, IMAGE_SIZE)

# Предобработка для EfficientNet
X_train = preprocess_input(X_train)
X_test = preprocess_input(X_test)

# Функция генерации данных
def create_data_generator(X, y, batch_size, shuffle=True):
    datagen = ImageDataGenerator()
    return datagen.flow(X, y, batch_size=batch_size, shuffle=shuffle)

train_generator = create_data_generator(X_train, y_train, BATCH_SIZE, shuffle=True)
test_generator = create_data_generator(X_test, y_test, BATCH_SIZE, shuffle=False)

# Определение MobileViT блока
# Определение MobileViT блока
class MobileViTBlock(layers.Layer):
    def __init__(self, num_filters, patch_size=(2, 2), **kwargs):
        super(MobileViTBlock, self).__init__(**kwargs)
        self.num_filters = num_filters
        self.patch_size = patch_size
        self.conv1x1 = layers.Conv2D(num_filters, kernel_size=1, activation='relu')  # Добавляем Conv2D

    def build(self, input_shape):
        c = input_shape[-1]
        if c is None:
            raise ValueError("Неизвестное количество каналов в MobileViTBlock. Проверьте входную модель.")

        patch_dims = self.patch_size[0] * self.patch_size[1] * c
        self.layer_norm = layers.LayerNormalization(axis=-1)
        self.mha = layers.MultiHeadAttention(num_heads=4, key_dim=patch_dims)
        super(MobileViTBlock, self).build(input_shape)

    def call(self, inputs):
        batch_size = tf.shape(inputs)[0]
        patches = tf.image.extract_patches(
            images=inputs, sizes=[1, self.patch_size[0], self.patch_size[1], 1],
            strides=[1, self.patch_size[0], self.patch_size[1], 1], rates=[1, 1, 1, 1], padding='VALID'
        )
        patches_shape = tf.shape(patches)
        num_patches = patches_shape[1] * patches_shape[2]
        patch_dims = patches.shape[-1]

        x = tf.reshape(patches, [batch_size, num_patches, patch_dims])
        x = self.layer_norm(x)
        x = self.mha(x, x) + x

        x = tf.reshape(x, [
            batch_size, patches_shape[1], self.patch_size[0], patches_shape[2], self.patch_size[1], -1
        ])
        x = tf.transpose(x, [0, 1, 3, 2, 4, 5])
        x = tf.reshape(x,
                       [batch_size, patches_shape[1] * self.patch_size[0], patches_shape[2] * self.patch_size[1], -1])

        x = self.conv1x1(x)  # Применяем свёрточный слой, чтобы задать фиксированное количество каналов
        return x

    def compute_output_shape(self, input_shape):
        return (
        input_shape[0], input_shape[1] // self.patch_size[0], input_shape[2] // self.patch_size[1], self.num_filters)

    def get_config(self):
        return {'num_filters': self.num_filters, 'patch_size': self.patch_size}


# Создание модели
def create_hybrid_model(input_shape=(256, 256, 3), num_classes=2):
    inputs = layers.Input(shape=input_shape)
    base_model = EfficientNetB0(include_top=False, input_shape=input_shape, weights='imagenet')
    base_model.trainable = False

    x = base_model(inputs)
    x = layers.Conv2D(128, kernel_size=1, activation='relu')(x)
    x = MobileViTBlock(num_filters=128, patch_size=(4, 4))(x)

    p3 = layers.Conv2D(128, 1)(x)
    p4 = layers.MaxPooling2D(pool_size=2)(p3)
    p4 = layers.Conv2D(128, 1)(p4)
    p4 = layers.UpSampling2D(size=(2, 2))(p4)

    p5 = layers.MaxPooling2D(pool_size=2)(p4)
    p5 = layers.Conv2D(128, 1)(p5)
    p5 = layers.UpSampling2D(size=(2, 2))(p5)

    x = layers.Concatenate()([p3, p4, p5])
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dense(256, activation="relu")(x)
    x = layers.Dropout(0.5)(x)
    outputs = layers.Dense(num_classes, activation="softmax")(x)

    return Model(inputs, outputs)

# Компиляция и обучение модели
model = create_hybrid_model(input_shape=(256, 256, 3), num_classes=2)
model.save("fire_detection_model.h5")

