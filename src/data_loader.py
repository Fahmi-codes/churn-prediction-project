import pandas as pd

df = pd.read_csv("data/customers.csv")

print("Total customers:", len(df))

print("\nColumns in dataset:")
print(df.columns)

print("\nChurn distribution:")
print(df["Churn"].value_counts())

print("\nChurn percentage:")
print(df["Churn"].value_counts(normalize=True) * 100)

print("\nAverage Monthly Charges:")
print(df["MonthlyCharges"].mean())