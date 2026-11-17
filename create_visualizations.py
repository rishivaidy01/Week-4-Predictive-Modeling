
import pandas as pd
import matplotlib.pyplot as plt
import os

print("Creating Logistics Optimization Visualizations...")

# Load optimization results
df = pd.read_csv("reports/optimization_analysis.csv")

# Create folder
os.makedirs("visualizations", exist_ok=True)

# Chart 1: Delivery Time Comparison
plt.figure(figsize=(10, 6))

plt.bar(
    df["Scenario"],
    df["Predicted_Delivery_Days"]
)

plt.title("Delivery Time Comparison Across Scenarios")
plt.xlabel("Optimization Scenario")
plt.ylabel("Predicted Delivery Time (Days)")
plt.xticks(rotation=25, ha="right")
plt.tight_layout()

plt.savefig("visualizations/optimization_comparison.png")
plt.close()


# Chart 2: Days Saved
plt.figure(figsize=(10, 6))

plt.bar(
    df["Scenario"],
    df["Days_Saved"]
)

plt.title("Delivery Days Saved Through Optimization")
plt.xlabel("Optimization Scenario")
plt.ylabel("Days Saved")

plt.xticks(rotation=25, ha="right")
plt.tight_layout()

plt.savefig("visualizations/days_saved.png")
plt.close()


# Chart 3: Original vs Combined Optimization
comparison = pd.DataFrame({
    "Scenario": ["Original", "Combined Optimization"],
    "Delivery_Days": [
        df.iloc[0]["Predicted_Delivery_Days"],
        df.iloc[4]["Predicted_Delivery_Days"]
    ]
})

plt.figure(figsize=(8, 6))

plt.bar(
    comparison["Scenario"],
    comparison["Delivery_Days"]
)

plt.title("Original vs Optimized Delivery Time")
plt.ylabel("Delivery Time (Days)")

plt.tight_layout()

plt.savefig("visualizations/original_vs_optimized.png")
plt.close()

print("\nAll charts created successfully!")

print("\nSaved Files:")
print("1. optimization_comparison.png")
print("2. days_saved.png")
print("3. original_vs_optimized.png")
