import pandas as pd

df = pd.read_csv("data/customers.csv")

# convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# check missing values
print("Missing values:")
print(df.isnull().sum())

# remove missing rows
df = df.dropna()

print("\nDataset shape after cleaning:")
print(df.shape)