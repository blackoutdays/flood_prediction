import pandas as pd
from sqlalchemy import create_engine

# Задайте путь к Excel файлу
excel_file = "/Users/aruka/Desktop/flood_prediction_ai/flood_results_excel/Zhezkazgan_r.xlsx"  # Укажите ваш файл

# Считываем данные из Excel
df = pd.read_excel(excel_file)

# Переименование колонок для удобства (если нужно)
df.columns = [
    "air_temp_avg", "air_temp_max", "air_temp_min",
    "soil_temp_avg", "soil_temp_max", "soil_temp_min",
    "dew_point_min", "vapor_pressure_avg", "humidity_avg", "humidity_min",
    "saturation_deficit_avg", "saturation_deficit_max",
    "pressure_station", "pressure_sea",
    "cloud_total", "cloud_lower",
    "wind_speed_avg", "wind_speed_max", "wind_speed_abs_max",
    "precipitation", "soil_condition_code",
    "snow_cover_state", "snow_cover_height_cm",
    "date", "flood_risk", "week", "flood_risk_week", "month", "flood_risk_month"
]

# Подключение к базе данных PostgreSQL
db_url = "postgresql://aruka:aruka@localhost:5432/flood_ai"
engine = create_engine(db_url)

# Укажите точное имя таблицы в базе данных
table_name = "predictions_Zhezkazgan"

# Записываем данные в таблицу
df.to_sql(table_name, engine, if_exists="append", index=False, schema="public")

print("Данные успешно загружены в таблицу!")