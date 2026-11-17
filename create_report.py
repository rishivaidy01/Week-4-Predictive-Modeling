
import os
import pandas as pd
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

print("Creating Week 4 Logistics Report...")

doc = Document()

# Document styling
style = doc.styles["Normal"]
style.font.name = "Arial"
style.font.size = Pt(10)

# Title
title = doc.add_heading(
    "WEEK 4: PREDICTIVE MODELING AND OPTIMIZATION IN LOGISTICS SYSTEMS",
    0
)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.add_run("Logistics Internship Project").bold = True

doc.add_paragraph("Prepared by: Rishi Vaidya")
doc.add_paragraph("Project: Predictive Modeling and Optimization")
doc.add_paragraph("Date: 16 November 2026")

# 1 Introduction
doc.add_heading("1. Introduction", level=1)
doc.add_paragraph(
    "This project focuses on predictive modeling and optimization "
    "in logistics systems. Machine learning techniques were used "
    "to estimate shipment delivery time and identify opportunities "
    "to improve logistics operations."
)

# 2 Objectives
doc.add_heading("2. Project Objectives", level=1)
objectives = [
    "Build a machine learning model to predict delivery time.",
    "Compare Linear Regression and Random Forest models.",
    "Evaluate model performance using MAE, RMSE and R2 Score.",
    "Apply 5-Fold Cross-Validation.",
    "Perform Random Forest hyperparameter tuning.",
    "Analyze optimization scenarios for logistics operations."
]
for item in objectives:
    doc.add_paragraph(item, style="List Bullet")

# 3 Dataset
doc.add_heading("3. Dataset Description", level=1)
doc.add_paragraph(
    "A simulated dataset containing 2,000 shipment records "
    "and 8 columns was generated using Python."
)

doc.add_paragraph("Features used:")
features = [
    "Distance_KM",
    "Shipment_Weight",
    "Transport_Mode",
    "Traffic_Level",
    "Weather",
    "Warehouse_Delay"
]
for item in features:
    doc.add_paragraph(item, style="List Bullet")

doc.add_paragraph(
    "Target variable: Delivery_Time. Shipment_ID was excluded "
    "from model training because it is an identifier."
)

# 4 Methodology
doc.add_heading("4. Methodology and Preprocessing", level=1)
doc.add_paragraph(
    "The dataset was loaded using Pandas. Categorical variables "
    "were converted using OneHotEncoder, while numerical variables "
    "were passed through using ColumnTransformer."
)
doc.add_paragraph(
    "The dataset was divided into 80% training records "
    "(1,600) and 20% testing records (400)."
)

# 5 Models
doc.add_heading("5. Machine Learning Models", level=1)
doc.add_paragraph(
    "Two algorithms were initially evaluated: Linear Regression "
    "and Random Forest Regressor. Random Forest was then tuned "
    "using GridSearchCV."
)

# 6 Evaluation
doc.add_heading("6. Model Performance Evaluation", level=1)

evaluation = pd.read_csv("reports/model_evaluation.csv")

table = doc.add_table(rows=1, cols=5)
table.style = "Table Grid"

headers = ["Model", "MAE", "RMSE", "R2 Score", "CV MAE"]
for i, header in enumerate(headers):
    table.rows[0].cells[i].text = header

for _, row in evaluation.iterrows():
    cells = table.add_row().cells
    cells[0].text = str(row["Model"])
    cells[1].text = f'{row["MAE"]:.3f}'
    cells[2].text = f'{row["RMSE"]:.3f}'
    cells[3].text = f'{row["R2_Score"]:.3f}'
    cells[4].text = f'{row["CV_MAE"]:.3f}'

best_model = evaluation.sort_values("MAE").iloc[0]

doc.add_paragraph(
    f'Best model: {best_model["Model"]}. '
    f'Test MAE: {best_model["MAE"]:.3f}, '
    f'RMSE: {best_model["RMSE"]:.3f}, '
    f'R2 Score: {best_model["R2_Score"]:.3f}.'
)

# 7 Cross Validation
doc.add_heading("7. Cross-Validation and Hyperparameter Tuning", level=1)
doc.add_paragraph(
    "Five-Fold Cross-Validation was applied to the training data. "
    "GridSearchCV tested 12 Random Forest parameter combinations "
    "across 5 folds, resulting in 60 fits."
)
doc.add_paragraph(
    "Best Random Forest parameters: n_estimators=200, "
    "max_depth=None, min_samples_split=2."
)
doc.add_paragraph(
    "The tuned Random Forest achieved a cross-validation MAE "
    "of approximately 0.866 days. Linear Regression remained "
    "the best model based on test MAE."
)

# 8 Optimization
doc.add_heading("8. Logistics Optimization Analysis", level=1)

optimization = pd.read_csv("reports/optimization_analysis.csv")

table2 = doc.add_table(rows=1, cols=3)
table2.style = "Table Grid"

for i, header in enumerate(
    ["Scenario", "Predicted Delivery Days", "Days Saved"]
):
    table2.rows[0].cells[i].text = header

for _, row in optimization.iterrows():
    cells = table2.add_row().cells
    cells[0].text = str(row["Scenario"])
    cells[1].text = f'{row["Predicted_Delivery_Days"]:.2f}'
    cells[2].text = f'{row["Days_Saved"]:.2f}'

doc.add_paragraph(
    "The original shipment prediction was 10.81 days. "
    "The combined optimization scenario reduced the predicted "
    "delivery time to 4.85 days, a modeled improvement of "
    "approximately 5.96 days."
)

# 9 Charts
doc.add_heading("9. Data Visualizations", level=1)

charts = [
    ("visualizations/optimization_comparison.png",
     "Delivery Time Comparison"),
    ("visualizations/days_saved.png",
     "Delivery Days Saved"),
    ("visualizations/original_vs_optimized.png",
     "Original vs Optimized Delivery Time")
]

for path, caption in charts:
    if os.path.exists(path):
        doc.add_paragraph(caption)
        doc.add_picture(path, width=Inches(5.8))

# 10 Recommendations
doc.add_heading("10. Optimization Recommendations", level=1)

recommendations = [
    "Reduce warehouse processing delays through better scheduling.",
    "Monitor traffic conditions and plan alternative routes.",
    "Use weather forecasts for proactive shipment planning.",
    "Evaluate transport mode according to delivery deadlines and cost.",
    "Monitor actual delivery performance and retrain models with real data."
]

for item in recommendations:
    doc.add_paragraph(item, style="List Bullet")

# 11 Limitations
doc.add_heading("11. Limitations", level=1)
doc.add_paragraph(
    "The dataset is simulated and not collected from a real logistics "
    "company. Delivery time was generated using predefined formulas "
    "and random noise. Therefore, model performance and optimization "
    "results demonstrate a learning experiment and should not be "
    "treated as verified real-world operational improvements. "
    "Transportation cost was not included as a model feature, so "
    "cost savings were not quantitatively calculated."
)

# 12 Conclusion
doc.add_heading("12. Conclusion", level=1)
doc.add_paragraph(
    "The project demonstrated how machine learning can support "
    "delivery time prediction and logistics planning. Linear "
    "Regression achieved the best test performance among the "
    "evaluated models. Cross-validation and hyperparameter tuning "
    "provided additional model evaluation. Scenario analysis "
    "highlighted the potential benefits of reducing warehouse "
    "delays and improving traffic and weather planning."
)

# Save report
doc.save("Week4_Report.docx")

print("\nWeek 4 Report created successfully!")
print("File: Week4_Report.docx")
