import os
import pandas as pd
from sqlalchemy import create_engine

FOLDER_PATH = os.path.dirname(__file__)
DB_URL = "postgresql://aruka:aruka@db:5432/flood_ai"
engine = create_engine(DB_URL)

COLUMNS = [
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

for file in os.listdir(FOLDER_PATH):
    if file.endswith(".xlsx"):
        city_name = file.replace("_r.xlsx", "").replace(".xlsx", "").lower()
        table_name = f"weatherdata_{city_name}"
        file_path = os.path.join(FOLDER_PATH, file)

        df = pd.read_excel(file_path)
        df.columns = COLUMNS

        df.to_sql(table_name, engine, if_exists="replace", index=False)
        print(f"[+] Загружен файл: {file} → таблица: {table_name}")