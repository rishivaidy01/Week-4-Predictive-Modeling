
import pandas as pd
import joblib

print("Loading Best Logistics Model...")

model = joblib.load("models/best_logistics_model.pkl")

# Sample shipment details
shipment = pd.DataFrame({
    "Distance_KM": [500],
    "Shipment_Weight": [100],
    "Transport_Mode": ["Road"],
    "Traffic_Level": ["High"],
    "Weather": ["Rainy"],
    "Warehouse_Delay": [2]
})

# Original delivery time prediction
original_prediction = model.predict(shipment)[0]

print("\nOriginal Shipment Details:")
print(shipment.to_string(index=False))
print("\nPredicted Delivery Time:",
      round(original_prediction, 2), "days")

# Optimization Scenario 1: Reduce warehouse delay
scenario_1 = shipment.copy()
scenario_1["Warehouse_Delay"] = 0

prediction_1 = model.predict(scenario_1)[0]

# Optimization Scenario 2: Improve traffic conditions
scenario_2 = shipment.copy()
scenario_2["Traffic_Level"] = "Low"

prediction_2 = model.predict(scenario_2)[0]

# Optimization Scenario 3: Improve weather conditions
scenario_3 = shipment.copy()
scenario_3["Weather"] = "Clear"

prediction_3 = model.predict(scenario_3)[0]

# Optimization Scenario 4: Combine improvements
scenario_4 = shipment.copy()
scenario_4["Warehouse_Delay"] = 0
scenario_4["Traffic_Level"] = "Low"
scenario_4["Weather"] = "Clear"

prediction_4 = model.predict(scenario_4)[0]

# Compare all scenarios
results = pd.DataFrame({
    "Scenario": [
        "Original",
        "Reduced Warehouse Delay",
        "Improved Traffic",
        "Clear Weather",
        "Combined Optimization"
    ],
    "Predicted_Delivery_Days": [
        original_prediction,
        prediction_1,
        prediction_2,
        prediction_3,
        prediction_4
    ]
})

results["Days_Saved"] = (
    original_prediction - results["Predicted_Delivery_Days"]
)

results["Predicted_Delivery_Days"] = (
    results["Predicted_Delivery_Days"].round(2)
)

results["Days_Saved"] = results["Days_Saved"].round(2)

print("\nOptimization Analysis:")
print(results.to_string(index=False))

# Save report
results.to_csv(
    "reports/optimization_analysis.csv",
    index=False
)

print("\nOptimization report saved successfully!")
