import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

file_path = "Training_data_r.xlsx"

df = pd.read_excel(file_path)

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

X_train, y_train = X, y
X_test, y_test = X, y

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

y_pred_train = np.clip(y_pred_train, 0, 100)
y_pred_test = np.clip(y_pred_test, 0, 100)

mae_train = mean_absolute_error(y_train, y_pred_train)
mae_test = mean_absolute_error(y_test, y_pred_test)
r2_train = r2_score(y_train, y_pred_train)
r2_test = r2_score(y_test, y_pred_test)

print(f"Train MAE: {mae_train:.2f}, R²: {r2_train:.2f}")
print(f"Test MAE: {mae_test:.2f}, R²: {r2_test:.2f}")



plt.figure(figsize=(10, 5))
indices = np.arange(len(y_test[:20]))
plt.bar(indices - 0.2, y_test[:20], width=0.4, label="Real values", alpha=0.7)
plt.bar(indices + 0.2, y_pred_test[:20], width=0.4, label="Predicted values", alpha=0.7)
plt.xticks(indices, indices)
plt.xlabel("Samples")
plt.ylabel("flood risk (%)")
plt.title("Comparison of model forecasts")
plt.legend()
plt.savefig("accuracy_bar_chart.png")
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(y_test[:20].values, label="Real values", marker="o", linestyle="-")
plt.plot(y_pred_test[:20], label="Predicted values", marker="s", linestyle="--")
plt.xlabel("Samples")
plt.ylabel("flood risk (%)")
plt.title("Comparison of model forecasts")
plt.legend()
plt.savefig("accuracy_line_chart.png")
plt.show()
