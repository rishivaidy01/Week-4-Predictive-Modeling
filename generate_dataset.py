
import pandas as pd
import numpy as np
import os

np.random.seed(42)

n = 2000

distance = np.random.randint(50, 2000, n)
weight = np.random.randint(1, 500, n)

transport = np.random.choice(
    ["Road", "Air", "Rail", "Sea"],
    n,
    p=[0.50, 0.20, 0.20, 0.10]
)

traffic = np.random.choice(
    ["Low", "Medium", "High"],
    n,
    p=[0.30, 0.45, 0.25]
)

weather = np.random.choice(
    ["Clear", "Rainy", "Stormy"],
    n,
    p=[0.60, 0.30, 0.10]
)

warehouse_delay = np.random.randint(0, 4, n)

# Transport mode effect
transport_effect = pd.Series(transport).map({
    "Road": 1.5,
    "Air": 0.5,
    "Rail": 2.0,
    "Sea": 4.0
}).to_numpy()

# Traffic effect
traffic_effect = pd.Series(traffic).map({
    "Low": 0,
    "Medium": 1,
    "High": 2.5
}).to_numpy()

# Weather effect
weather_effect = pd.Series(weather).map({
    "Clear": 0,
    "Rainy": 1.5,
    "Stormy": 3
}).to_numpy()

# Target variable: Delivery Time
delivery_time = (
    1
    + distance / 250
    + weight / 300
    + transport_effect
    + traffic_effect
    + weather_effect
    + warehouse_delay
    + np.random.normal(0, 0.8, n)
)

delivery_time = np.maximum(delivery_time, 1)

df = pd.DataFrame({
    "Shipment_ID": range(1001, 1001 + n),
    "Distance_KM": distance,
    "Shipment_Weight": weight,
    "Transport_Mode": transport,
    "Traffic_Level": traffic,
    "Weather": weather,
    "Warehouse_Delay": warehouse_delay,
    "Delivery_Time": delivery_time.round(2)
})

os.makedirs("data", exist_ok=True)

df.to_csv("data/predictive_logistics_dataset.csv", index=False)

print("Predictive Dataset Generated Successfully!")
print("Total Rows:", df.shape[0])
print("Total Columns:", df.shape[1])
print("\nFirst 5 Records:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:", df.isnull().sum().sum())
