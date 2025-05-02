import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Load the data
df = pd.read_csv("dorm_capacity.csv")

# Train model
X = df[["Year"]]
y = df["DormCapacity"]
model = LinearRegression()
model.fit(X, y)

# Predict future years
future_years = pd.DataFrame({"Year": np.arange(2025, 2031)})
predictions = model.predict(future_years)

# Plot
plt.plot(df["Year"], df["DormCapacity"], label="Actual", marker="o")
plt.plot(future_years["Year"], predictions, label="Predicted", marker="x")
plt.xlabel("Year")
plt.ylabel("Dorm Capacity")
plt.title("UC Merced Dorm Capacity Prediction")
plt.legend()
plt.grid(True)
plt.show()

# Print predictions
for year, prediction in zip(future_years["Year"], predictions):
    print(f"{year}: {int(prediction)} beds")
