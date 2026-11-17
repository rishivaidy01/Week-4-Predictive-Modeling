
import pandas as pd
import numpy as np
import os
import joblib

from sklearn.model_selection import (
    train_test_split,
    cross_val_score,
    KFold,
    GridSearchCV
)

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

print("Loading Dataset...")

df = pd.read_csv("data/predictive_logistics_dataset.csv")

# Features and target
X = df.drop(columns=["Shipment_ID", "Delivery_Time"])
y = df["Delivery_Time"]

categorical_features = [
    "Transport_Mode",
    "Traffic_Level",
    "Weather"
]

numerical_features = [
    "Distance_KM",
    "Shipment_Weight",
    "Warehouse_Delay"
]

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ("num", "passthrough", numerical_features)
    ]
)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

print("Training Records:", len(X_train))
print("Testing Records:", len(X_test))

# 5-Fold Cross Validation
cv = KFold(n_splits=5, shuffle=True, random_state=42)

# Models
models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(
        n_estimators=100,
        max_depth=12,
        random_state=42,
        n_jobs=-1
    )
}

results = []
trained_models = {}

# Train and evaluate models
for name, algorithm in models.items():

    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", algorithm)
    ])

    pipeline.fit(X_train, y_train)

    predictions = pipeline.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)

    # 5-Fold Cross Validation MAE
    cv_scores = cross_val_score(
        pipeline,
        X_train,
        y_train,
        cv=cv,
        scoring="neg_mean_absolute_error",
        n_jobs=-1
    )

    cv_mae = -cv_scores.mean()

    trained_models[name] = pipeline

    results.append({
        "Model": name,
        "MAE": mae,
        "RMSE": rmse,
        "R2_Score": r2,
        "CV_MAE": cv_mae
    })

    print("\nModel:", name)
    print("Test MAE:", round(mae, 3))
    print("Test RMSE:", round(rmse, 3))
    print("R2 Score:", round(r2, 3))
    print("5-Fold CV MAE:", round(cv_mae, 3))


# Hyperparameter Tuning for Random Forest
print("\nStarting Hyperparameter Tuning...")

rf_pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", RandomForestRegressor(
        random_state=42,
        n_jobs=-1
    ))
])

param_grid = {
    "model__n_estimators": [100, 200],
    "model__max_depth": [8, 12, None],
    "model__min_samples_split": [2, 5]
}

grid_search = GridSearchCV(
    estimator=rf_pipeline,
    param_grid=param_grid,
    cv=cv,
    scoring="neg_mean_absolute_error",
    n_jobs=-1,
    verbose=1
)

grid_search.fit(X_train, y_train)

best_rf_model = grid_search.best_estimator_

print("\nBest Random Forest Parameters:")
print(grid_search.best_params_)

print(
    "Best Cross Validation MAE:",
    round(-grid_search.best_score_, 3)
)

# Evaluate tuned Random Forest on test data
tuned_predictions = best_rf_model.predict(X_test)

tuned_mae = mean_absolute_error(y_test, tuned_predictions)
tuned_rmse = np.sqrt(mean_squared_error(y_test, tuned_predictions))
tuned_r2 = r2_score(y_test, tuned_predictions)

results.append({
    "Model": "Tuned Random Forest",
    "MAE": tuned_mae,
    "RMSE": tuned_rmse,
    "R2_Score": tuned_r2,
    "CV_MAE": -grid_search.best_score_
})

trained_models["Tuned Random Forest"] = best_rf_model

print("\nTuned Random Forest Results:")
print("MAE:", round(tuned_mae, 3))
print("RMSE:", round(tuned_rmse, 3))
print("R2 Score:", round(tuned_r2, 3))

# Select best model using lowest test MAE
results_df = pd.DataFrame(results)
results_df = results_df.sort_values("MAE")

best_model_name = results_df.iloc[0]["Model"]
best_model = trained_models[best_model_name]

# Save outputs
os.makedirs("models", exist_ok=True)
os.makedirs("reports", exist_ok=True)

joblib.dump(best_model, "models/best_logistics_model.pkl")

results_df.to_csv(
    "reports/model_evaluation.csv",
    index=False
)

# Save predictions of selected model
best_predictions = best_model.predict(X_test)

prediction_results = pd.DataFrame({
    "Actual_Delivery_Time": y_test.values,
    "Predicted_Delivery_Time": best_predictions.round(2)
})

prediction_results.to_csv(
    "reports/prediction_results.csv",
    index=False
)

print("\nFinal Model Comparison:")
print(results_df.round(3).to_string(index=False))

print("\nBest Model:", best_model_name)
print("Model saved successfully!")
print("Evaluation reports saved successfully!")
