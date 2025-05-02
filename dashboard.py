import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

# Load dataset
df = pd.read_csv("enrollment_full.csv")

# Train model
features = ["Year", "AcceptanceRate", "YieldRate", "DormCapacity", "Applications"]
X = df[features]
y = df["Enrollment"]

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Streamlit UI
st.title("UC Merced Enrollment Prediction Dashboard")
st.markdown("Adjust future variables to see how UC Merced's enrollment might change.")

# Sliders for 2030 inputs
year = 2030
accept_rate = st.slider("Acceptance Rate (%)", 60, 100, 94)
yield_rate = st.slider("Yield Rate (%)", 5, 80, 30)
dorm_capacity = st.slider("Dorm Capacity", 4000, 10000, 6200)
applications = st.slider("Applications", 20000, 100000, 38000)

# Predict
input_df = pd.DataFrame({
    "Year": [year],
    "AcceptanceRate": [accept_rate],
    "YieldRate": [yield_rate],
    "DormCapacity": [dorm_capacity],
    "Applications": [applications]
})
pred = model.predict(input_df)[0]

# Show result
st.subheader(f"📈 Predicted Enrollment for {year}: **{int(pred):,} students**")

# Plot actual + predicted
future_years = [2025, 2026, 2027, 2028, 2029]
future_data = pd.DataFrame({
    "Year": future_years + [year],
    "AcceptanceRate": [91, 92, 92, 93, 93, accept_rate],
    "YieldRate": [34, 33, 32, 32, 31, yield_rate],
    "DormCapacity": [5200, 5400, 5600, 5800, 6000, dorm_capacity],
    "Applications": [28000, 30000, 32000, 34000, 36000, applications]
})
future_pred = model.predict(future_data)

combined_years = df["Year"].tolist() + future_data["Year"].tolist()
combined_enrollment = df["Enrollment"].tolist() + future_pred.tolist()

fig, ax = plt.subplots()
ax.plot(combined_years, combined_enrollment, marker='o')
ax.set_title("UC Merced Enrollment Projection")
ax.set_xlabel("Year")
ax.set_ylabel("Enrollment")
st.pyplot(fig)
