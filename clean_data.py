import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

# Drop unnecessary columns (if present)
df = df.drop(columns=["id", "Unnamed: 32"], errors="ignore")

# Convert diagnosis labels
df["diagnosis"] = df["diagnosis"].map({"M": "Malignant", "B": "Benign"})

# Save cleaned file
df.to_csv("cancer_cleaned.csv", index=False)

print("Cleaned file created successfully!")
