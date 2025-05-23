import pandas as pd
from prophet import Prophet

# Загружаем данные
df = pd.read_excel("Data excel/Актау_final_cleaned.xlsx")
df['Дата'] = pd.to_datetime(df['Дата'])

# Добавляем вспомогательные колонки
df['Год'] = df['Дата'].dt.year
df['День_Месяц'] = df['Дата'].dt.strftime('%m-%d')

# Определяем диапазон прогнозирования
forecast_start_date = pd.to_datetime("2024-09-01")
forecast_end_date = pd.to_datetime("2025-09-01")
forecast_dates = pd.date_range(start=forecast_start_date, end=forecast_end_date, freq='D')

forecast_data = []

# Столбцы, для которых считаем средние значения
columns_with_mean = ["Количество осадков, мм", "Сост.повер почвы, шифр", "Снежный покров. Ст.покр.", "Снежный покров. Высота, см"]

for date in forecast_dates:
    day_month = date.strftime('%m-%d')
    current_year = date.year

    # Выбираем, за сколько лет брать данные (за 1-3 года)
    if date.month in [9, 10]:
        historical_years = [current_year - 1, current_year - 2]
    else:
        historical_years = [current_year - 1, current_year - 2, current_year - 3]

    historical_data = df[(df['День_Месяц'] == day_month) & (df['Год'].isin(historical_years))]

    if not historical_data.empty:
        mean_values = historical_data.mean(numeric_only=True)
        mean_values['Дата'] = date
        forecast_data.append(mean_values)

forecast_df = pd.DataFrame(forecast_data)
forecast_df = forecast_df.round(1)
forecast_df.drop(columns=['Год'], inplace=True, errors='ignore')

# Сохраняем средние значения в Excel
forecast_df.to_excel("Data to AI/Просто.xlsx", index=False)

# Теперь прогнозируем остальные параметры через Prophet
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
columns_for_prophet = [col for col in numeric_columns if col not in columns_with_mean]

all_forecasts = pd.DataFrame()

for column in numeric_columns:
    print(f"Прогнозирование для параметра: {column}")

    temp_df = df[[column]].reset_index().rename(columns={"Дата": "ds", column: "y"})

    # 🔹 Отладка перед обучением 🔹
    print(f"Прогнозируемый столбец: {column}")
    print(temp_df.dtypes)  # Проверяем типы данных
    print(temp_df.head())  # Вывод первых строк

    # Проверка NaN
    print(temp_df.isnull().sum())

    # Заполняем пропуски (если есть)
    temp_df["y"].fillna(temp_df["y"].mean(), inplace=True)

    model = Prophet()
    model.fit(temp_df)  # Prophet требует "ds" и "y"


# Объединяем два прогноза (средние значения + Prophet)
final_forecast = all_forecasts.merge(forecast_df, on="ds", how="outer")

# Сохраняем итоговый прогноз
final_forecast.to_excel("Data to AI/только_прогнозы(2).xlsx", index=False)

# Выводим несколько строк результата
print(final_forecast.head())



