import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sympy import false

training_file = "Training_data_r.xlsx"
new_data_file = "Data to AI/Zhezkazgan.xlsx"
output_file = "Flood_results/Zhezkazgan_r.xlsx"

has_water_body = False

training_data = pd.read_excel(training_file)
new_data = pd.read_excel(new_data_file)

X_train = training_data.drop(columns=["Риск паводков"])
y_train = training_data["Риск паводков"]

assert all(col in new_data.columns for col in X_train.columns), \
    "В новых данных отсутствуют некоторые признаки, необходимые для прогноза!"

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

new_data_for_prediction = new_data[X_train.columns]
new_data_predictions = model.predict(new_data_for_prediction)

new_data["Риск паводков"] = new_data_predictions.clip(0, 100).round(2)

def apply_adjustments(row):
    date = pd.to_datetime(row["Дата"])
    month = date.month
    day = date.day
    risk = row["Риск паводков"]

    if has_water_body:
        if month in [3, 4, 5]:
            risk *= 1.3
        elif month in [6, 7, 8]:
            risk *= 1.2
        elif month in [9, 10, 11]:
            risk *= 1.1
    else:
        risk *= 0.7

    if month in [12, 1] or (month == 2 and day <= 20):
        risk *= 0.4
    elif month == 2 and 20 < day <= 25:
        risk *= 0.65
    elif month == 2 and day > 25:
        risk *= 0.85

    return min(round(risk, 2), 100)

new_data["Риск паводков скорректированный"] = new_data.apply(apply_adjustments, axis=1)

new_data.drop(columns=["Риск паводков"], inplace=True)
new_data.rename(columns={"Риск паводков скорректированный": "Риск паводков"}, inplace=True)

new_data["Неделя"] = pd.to_datetime(new_data["Дата"]).dt.isocalendar().week
new_data["Месяц"] = pd.to_datetime(new_data["Дата"]).dt.month

new_data["Риск паводков (неделя)"] = new_data.groupby("Неделя")["Риск паводков"].transform("mean").round(2)
new_data["Риск паводков (месяц)"] = new_data.groupby("Месяц")["Риск паводков"].transform("mean").round(2)

new_data.to_excel(output_file, index=False)
print(f"Прогнозы успешно сохранены в файл {output_file}.")

