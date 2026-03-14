import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Load and clean data
df = pd.read_csv("data/customers.csv")
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df = df.dropna()

# Encode target
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

# Select features
features = ["tenure", "MonthlyCharges", "TotalCharges"]
X = df[features]
y = df["Churn"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "models/churn_model.pkl")

print("Model trained and saved!")