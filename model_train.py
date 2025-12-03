import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

# Load data
df = pd.read_csv("synthetic_contract_data.csv")

# Features and target
X = df.drop("Total Contract Value", axis=1)
y = df["Total Contract Value"]

# Identify categorical columns
categorical_cols = X.columns.tolist()

# Preprocessing: one-hot encoding
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols)
    ]
)

# Build model pipeline
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("regressor", RandomForestRegressor(n_estimators=200, random_state=42)),
    ]
)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Train
model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)
mae = mean_absolute_error(y_test, preds)
print(f"Mean Absolute Error: ${mae:,.0f}")

# Save predictions to Excel
output_df = X_test.copy()
output_df["Actual Total Contract Value"] = y_test.values
output_df["Predicted Total Contract Value"] = preds

output_df.to_excel("predicted_contract_values.xlsx", index=False)

# Save model (optional)
joblib.dump(model, "contract_value_model.pkl")

print("Predictions saved to predicted_contract_values.xlsx")
