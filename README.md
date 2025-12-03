# Government-Contract-Value-Prediction-Model
This repository demonstrates how I designed and collaborated on a machine learning workflow that categorizes and analyzes government contract data for the health sector. The example is **fully recreated with synthetic data** to reflect my technical fluency, while avoiding any proprietary or confidential information.

---

## 🎯 Project Overview

In my previous role, I partnered with engineering and data science teams to build a machine learning model that analyzed federal and state government contracts in the healthcare domain. The goal was to:

- Understand patterns across contract types and agencies  
- Build structured datasets from heterogeneous contract files  
- Predict contract attributes (e.g., value range or market segment)  
- Support internal market analytics and BD strategy

This repository provides a **safe, non-proprietary reconstruction** of that workflow using:

- **Synthetic data**
- **Simplified ML modeling techniques**
- **A reproducible pipeline**

---

## 📊 Dataset (Synthetic)

The `synthetic_contract_data.csv` file mirrors the structure of real government healthcare contracts. Columns include:

- Contract Name  
- Contract Number  
- Task/Delivery Order Number  
- Modification Number  
- Principal Contract Requirement  
- Keyword Search Field  
- Product Service Code  
- Contracting Agency  
- Total Contract Value (target variable)

All values are entirely fabricated.

---

## 🧠 Machine Learning Approach

This demo uses a standard ML workflow:

1. **Data ingestion**  
2. **Categorical encoding** using one-hot encoding  
3. **Model training** with `RandomForestRegressor`  
4. **Train/test split** for validation  
5. **Prediction output** exported to Excel

The outcome is an Excel file containing:

- Original contract fields  
- Actual total contract value  
- Predicted total contract value  

---

## 🛠 Technical Stack

- Python  
- Pandas  
- scikit-learn  
- Joblib  
- Excel export (`pandas.to_excel`)

