import subprocess
import sys
import numpy  # linear algebra
import pandas  # data processing, CSV file I/O (e.g. pd.read_csv)
import os

# Установка пакетов вынесена в install_packages() torch torchvision albumentations pillow opencv-python

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.efficientnet import preprocess_input
from pathlib import Path
import numpy as np
import cv2

# Paths to image directories
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


# Constants
IMAGE_SIZE = (256, 256)
BATCH_SIZE = 32
LABELS = {"Fire": 0, "NonFire": 1}


def load_images_from_directory(directory_path, label, image_size):
    """Loads and preprocesses images from a directory."""
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
    """Loads and combines images and labels from specified paths."""
    images, labels = [], []
    for label_name, label_path in data_paths.items():
        class_images, class_labels = load_images_from_directory(label_path, labels_dict[label_name], image_size)
        images.append(class_images)
        labels.append(class_labels)
    return np.concatenate(images), np.concatenate(labels)

# Load training and test datasets
X_train, y_train = prepare_dataset(DATA_PATHS["train"], LABELS, IMAGE_SIZE)
X_test, y_test = prepare_dataset(DATA_PATHS["test"], LABELS, IMAGE_SIZE)

# Preprocess input for EfficientNet
X_train = preprocess_input(X_train)
X_test = preprocess_input(X_test)

# Print dataset size information
print(f"Number of train images: {len(X_train)}")
print(f"Number of test images: {len(X_test)}")

def create_data_generator(X, y, batch_size, shuffle=True):
    """Creates a data generator for batches of images and labels."""
    datagen = ImageDataGenerator()
    return datagen.flow(X, y, batch_size=batch_size, shuffle=shuffle)

# Create train and test data generators
train_generator = create_data_generator(X_train, y_train, BATCH_SIZE, shuffle=True)
test_generator = create_data_generator(X_test, y_test, BATCH_SIZE, shuffle=False)

# Example of iterating through the DataLoader
for images, labels in train_generator:
    print("Batch shape:", images.shape, labels.shape)  # Expected: (BATCH_SIZE, 256, 256, 3)
    break  # Display only the first batch

import tensorflow as tf
from tensorflow.keras import layers, Model
from tensorflow.keras.applications import EfficientNetB0

# Custom MobileViT Block with corrected get_config
class MobileViTBlock(layers.Layer):
    def __init__(self, num_filters, patch_size=(2, 2), **kwargs):
        super(MobileViTBlock, self).__init__(**kwargs)
        self.num_filters = num_filters
        self.patch_size = patch_size

    def build(self, input_shape):
        c = input_shape[-1]
        if c is None:
            raise ValueError("The channel dimension of the inputs should be defined.")
        patch_dims = self.patch_size[0] * self.patch_size[1] * c

        self.layer_norm = layers.LayerNormalization(axis=-1)
        self.mha = layers.MultiHeadAttention(num_heads=4, key_dim=patch_dims)
        super(MobileViTBlock, self).build(input_shape)

    def call(self, inputs):
        batch_size = tf.shape(inputs)[0]
        h, w = tf.shape(inputs)[1], tf.shape(inputs)[2]
        c = inputs.shape[-1]

        # Create patches
        patches = tf.image.extract_patches(
            images=inputs,
            sizes=[1, self.patch_size[0], self.patch_size[1], 1],
            strides=[1, self.patch_size[0], self.patch_size[1], 1],
            rates=[1, 1, 1, 1],
            padding='VALID'
        )
        patches_shape = tf.shape(patches)
        num_patches = patches_shape[1] * patches_shape[2]
        patch_dims = patches.shape[-1]

        x = tf.reshape(patches, [batch_size, num_patches, patch_dims])

        # Transformer block
        x_input = x  # For residual connection
        x = self.layer_norm(x)
        x = self.mha(x, x)
        x = x + x_input  # Residual connection

        # Reshape back to feature map
        x = tf.reshape(x, [
            batch_size,
            patches_shape[1],
            patches_shape[2],
            self.patch_size[0],
            self.patch_size[1],
            c
        ])
        x = tf.transpose(x, [0, 1, 3, 2, 4, 5])
        x = tf.reshape(x, [batch_size, patches_shape[1] * self.patch_size[0], patches_shape[2] * self.patch_size[1], c])

        return x

    def get_config(self):
        config = super(MobileViTBlock, self).get_config()
        config.update({
            'num_filters': self.num_filters,
            'patch_size': self.patch_size,
        })
        return config



# EfficientNet Backbone
def efficientnet_base(input_shape):
    base_model = EfficientNetB0(include_top=False, input_shape=input_shape, weights='imagenet')
    base_model.trainable = False  # Freeze base layers
    return base_model

# Hybrid Model Architecture with corrected FPN
def create_hybrid_model(input_shape=(256, 256, 3), num_classes=2):
    inputs = layers.Input(shape=input_shape)
    
    # EfficientNet Backbone
    base_model = efficientnet_base(input_shape)
    x = base_model(inputs)
    
    # Reduce channels to a known dimension
    x = layers.Conv2D(128, kernel_size=1, activation='relu')(x)
    
    # MobileViT block
    x = MobileViTBlock(num_filters=128, patch_size=(4, 4))(x)
    
    # FPN for Multi-Resolution Feature Extraction
    p3 = layers.Conv2D(128, 1)(x)  # Shape: (None, 8, 8, 128)

    # Downsample p3 to get p4
    p4 = layers.MaxPooling2D(pool_size=2)(p3)  # Shape: (None, 4, 4, 128)
    p4 = layers.Conv2D(128, 1)(p4)
    # Upsample p4 back to (8, 8)
    p4 = layers.UpSampling2D(size=(2, 2))(p4)  # Shape: (None, 8, 8, 128)

    # Downsample p4 to get p5
    p5 = layers.MaxPooling2D(pool_size=2)(p4)  # Shape: (None, 4, 4, 128)
    p5 = layers.Conv2D(128, 1)(p5)
    # Upsample p5 back to (8, 8)
    p5 = layers.UpSampling2D(size=(2, 2))(p5)  # Shape: (None, 8, 8, 128)

    # Concatenate features from different resolutions
    x = layers.Concatenate()([p3, p4, p5])  # Now shapes match: (None, 8, 8, 384)
    x = layers.GlobalAveragePooling2D()(x)

    # Classification Head
    x = layers.Dense(256, activation="relu")(x)
    x = layers.Dropout(0.5)(x)
    outputs = layers.Dense(num_classes, activation="softmax")(x)

    # Build Model
    model = Model(inputs, outputs)
    return model

# Model Compilation
model = create_hybrid_model(input_shape=(256, 256, 3), num_classes=2)
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              loss='sparse_categorical_crossentropy', metrics=['accuracy'])

from tensorflow.keras.utils import get_custom_objects

get_custom_objects().update({'MobileViTBlock': MobileViTBlock})

import tensorflow as tf
import matplotlib.pyplot as plt

# Callbacks (if you're using them)
early_stopping = tf.keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True)
model_checkpoint = tf.keras.callbacks.ModelCheckpoint('best_model.h5', save_best_only=True)

# Training the model
history = model.fit(
    train_generator,
    epochs=30,
    validation_data=test_generator,
    callbacks=[early_stopping, model_checkpoint]

)
# Plotting training & validation accuracy and loss
def plot_training_history(history):
    """Plot training and validation accuracy and loss."""
    epochs = range(len(history.history['accuracy']))

    # Plot accuracy
    plt.figure()
    plt.plot(epochs, history.history['accuracy'], label='Training Accuracy')
    plt.plot(epochs, history.history['val_accuracy'], label='Validation Accuracy')
    plt.title('Training and Validation Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()

    # Plot loss
    plt.figure()
    plt.plot(epochs, history.history['loss'], label='Training Loss')
    plt.plot(epochs, history.history['val_loss'], label='Validation Loss')
    plt.title('Training and Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()

# Display the graphs
plot_training_history(history)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# True labels are available directly as `y_test`
y_true = y_test

# Generate predictions on the test dataset
y_pred_probs = model.predict(test_generator)  # Predicted probabilities
y_pred = np.argmax(y_pred_probs, axis=1)  # Predicted labels

# Compute accuracy, precision, recall, and F1 score
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, average='binary')  # Use 'macro' or 'weighted' for multi-class
recall = recall_score(y_true, y_pred, average='binary')
f1 = f1_score(y_true, y_pred, average='binary')

print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")

# Classification report
print("\nClassification Report:")
print(classification_report(y_true, y_pred, target_names=["Fire", "NonFire"]))

# Confusion matrix
conf_matrix = confusion_matrix(y_true, y_pred)
print("\nConfusion Matrix:")
print(conf_matrix)

# Plotting the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=["Fire", "NonFire"], yticklabels=["Fire", "NonFire"])
plt.xlabel("Predicted Labels")
plt.ylabel("True Labels")
plt.title("Confusion Matrix")
plt.show()