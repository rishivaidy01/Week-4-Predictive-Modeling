
# Week 4 - Predictive Modeling and Optimization in Logistics Systems

## Project Overview
This project focuses on predicting shipment delivery time using Machine Learning and analyzing optimization strategies for logistics operations.

## Objectives
- Predict shipment delivery time.
- Compare Linear Regression and Random Forest.
- Evaluate models using MAE, RMSE and R2 Score.
- Apply 5-Fold Cross-Validation.
- Perform Hyperparameter Tuning using GridSearchCV.
- Analyze logistics optimization scenarios.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Python-docx

## Dataset
The project uses a simulated dataset containing 2,000 shipment records.

Features:
- Distance_KM
- Shipment_Weight
- Transport_Mode
- Traffic_Level
- Weather
- Warehouse_Delay

Target:
- Delivery_Time

## Machine Learning Models
1. Linear Regression
2. Random Forest Regressor
3. Tuned Random Forest

## Best Model Results
Linear Regression achieved the best test performance:

- MAE: 0.677 days
- RMSE: 0.856 days
- R2 Score: 0.924
- 5-Fold CV MAE: 0.642 days

## Optimization Analysis
The combined optimization scenario reduced predicted delivery time from 10.81 days to 4.85 days in the sample scenario.

## Project Structure
- data/ : Dataset
- models/ : Saved machine learning model
- reports/ : Evaluation and optimization reports
- visualizations/ : Generated charts
- generate_dataset.py
- train_model.py
- optimization_analysis.py
- create_visualizations.py
- create_report.py
- Week4_Report.docx

## How to Run

Install required libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn python-docx joblib
```

Generate dataset:

```bash
python generate_dataset.py
```

Train models:

```bash
python train_model.py
```

Run optimization:

```bash
python optimization_analysis.py
```

Create visualizations:

```bash
python create_visualizations.py
```

Generate final report:

```bash
python create_report.py
```

## Important Note
This project uses simulated data for educational purposes. Results are not verified real-world logistics performance or guaranteed operational savings.
