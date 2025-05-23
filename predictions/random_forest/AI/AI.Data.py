import pandas as pd

df = pd.read_excel("Data excel/Актау_final_cleaned.xlsx")

df['Дата'] = pd.to_datetime(df['Дата'])

df['Год'] = df['Дата'].dt.year
df['День_Месяц'] = df['Дата'].dt.strftime('%m-%d')

forecast_start_date = pd.to_datetime("2024-09-01")
forecast_end_date = pd.to_datetime("2025-09-01")
forecast_dates = pd.date_range(start=forecast_start_date, end=forecast_end_date, freq='D')

forecast_data = []

for date in forecast_dates:
    day_month = date.strftime('%m-%d')
    current_year = date.year

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

forecast_df.to_excel("Data to AI/Example.xlsx", index=False)

print(forecast_df.head())
print(f"Processing forecast for date: {date}")
print(f"Historical data found: {historical_data.shape[0]} records")

