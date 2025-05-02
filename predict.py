import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

df = pd.read_csv("ucm_enrollment.csv")

X = df[["Year"]]
y = df["Enrollment"]
model = LinearRegression()
model.fit(X, y)

future_years = pd.DataFrame({"Year": np.arange(2025, 2031)})
future_predictions = model.predict(future_years)

plt.plot(df["Year"], df["Enrollment"], label="Actual", marker="o")
plt.plot(future_years["Year"], future_predictions, label="Predicted", marker="x")
plt.xlabel("Year")
plt.ylabel("Enrollment")
plt.title("UC Merced Enrollment Prediction")
plt.legend()
plt.grid(True)
plt.show()

for year, prediction in zip(future_years["Year"], future_predictions):
    print(f"{year}: {int(prediction)} students")
