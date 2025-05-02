import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

# Step 1: Load the dataset
df = pd.read_csv("enrollment_full.csv")

# Step 2: Prepare features and target
features = ["Year", "AcceptanceRate", "YieldRate", "DormCapacity", "Applications"]
X = df[features]
y = df["Enrollment"]

# Step 3: Train/test split (to evaluate accuracy)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train a Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 5: Evaluate model
pred_test = model.predict(X_test)
rmse = mean_squared_error(y_test, pred_test, squared=False)
print(f"RMSE: {rmse:.2f}")

# Step 6: Predict future years
future_data = pd.DataFrame({
    "Year": [2025, 2026, 2027, 2028, 2029, 2030],
    "AcceptanceRate": [91, 92, 92, 93, 93, 94],  # hypothetical
    "YieldRate": [34, 33, 32, 32, 31, 30],       # hypothetical
    "DormCapacity": [5200, 5400, 5600, 5800, 6000, 6200],
    "Applications": [28000, 30000, 32000, 34000, 36000, 38000]
})

future_pred = model.predict(future_data)

# Step 7: Plot
plt.plot(df["Year"], df["Enrollment"], label="Actual", marker="o")
plt.plot(future_data["Year"], future_pred, label="Predicted", marker="x")
plt.xlabel("Year")
plt.ylabel("Enrollment")
plt.title("UC Merced Enrollment Forecast (Multi-Feature Model)")
plt.legend()
plt.grid(True)
plt.show()

# Step 8: Print future predictions
for year, val in zip(future_data["Year"], future_pred):
    print(f"{year}: {int(val)} students")
