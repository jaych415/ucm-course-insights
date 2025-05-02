import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Load the data
df = pd.read_csv("acceptance_rate.csv")

# Train the model
X = df[["Year"]]
y = df["AcceptanceRate"]
model = LinearRegression()
model.fit(X, y)

# Predict future years
future_years = pd.DataFrame({"Year": np.arange(2025, 2031)})
predictions = model.predict(future_years)

# Plot
plt.plot(df["Year"], df["AcceptanceRate"], label="Actual", marker="o")
plt.plot(future_years["Year"], predictions, label="Predicted", marker="x")
plt.xlabel("Year")
plt.ylabel("Acceptance Rate (%)")
plt.title("UC Merced Acceptance Rate Prediction")
plt.legend()
plt.grid(True)
plt.show()

# Print predictions
for year, prediction in zip(future_years["Year"], predictions):
    print(f"{year}: {prediction:.2f}%")
