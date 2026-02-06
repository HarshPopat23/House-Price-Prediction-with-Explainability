# 🏠 House Price Prediction with Explainability

## 📌 Project Overview

This project predicts house prices using the Ames Housing dataset.
Multiple ensemble regression models are trained and evaluated,
with feature correlation analysis for explainability.

## 📊 Dataset

- Ames Housing Dataset
- 2,900+ records
- 80+ features

## 🧹 Data Preprocessing

- Dropped high-missing categorical columns
- Mean imputation for numerical features
- Mode imputation for categorical features
- One-hot encoding
- Feature scaling using StandardScaler

## 🧠 Feature Selection

- Pearson correlation with target variable
- Top 20 correlated features selected

## 🤖 Models Used

- Random Forest Regressor
- Gradient Boosting Regressor
- HistGradientBoosting Regressor

## 📈 Evaluation Metrics

- R² Score
- RMSE (Root Mean Squared Error)

## 🏆 Results

| Model                | Test R² | RMSE |
| -------------------- | ------- | ---- |
| Random Forest        | XX      | XX   |
| Gradient Boosting    | XX      | XX   |
| HistGradientBoosting | XX      | XX   |

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn

## 🚀 How to Run

```bash
pip install -r requirements.txt
python src/train_models.py
```
