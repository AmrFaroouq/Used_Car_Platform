"""
import pandas as pd 

df = pd.read_csv("data/pre-owned cars.csv")
print(df.head())

print(df.head())

print("Dataset shape :" , df.shape)

print("column names :")
print(df.columns.tolist())

print(df.info())
"""

import pandas as pd

# Load dataset
df = pd.read_csv("data/pre-owned cars.csv")

# 1. Dataset dimensions
print("Dataset shape:", df.shape)

# 2. Missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# 3. Duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

# 4. Data types
print("\nData types:")
print(df.dtypes)

# 5. Statistical summary
print("\nStatistical summary:")
print(df.describe(include="all").T)

# 6. Sample data
print("\nFirst 5 rows:")
print(df.head())

df_clean = df.copy()
print("Original dataset shape" , df_clean.shape)
df_clean = df_clean.drop_duplicates()

print("\nDataset shape before cleaning:")
print(df_clean.isnull().sum())

df_clean = df_clean.dropna(subset=["brand" , "model"])

df_clean["engine_capacity(CC)"] = df_clean["engine_capacity(CC)"].fillna(
    df_clean["engine_capacity(CC)"].median()
)

print("\nMissing values after cleaning:")
print(df_clean.isnull().sum())

print("\nDataset shape after cleaning:")
print(df_clean.shape)

print("\nMake year sample:")
print(df_clean[["make_year", "reg_year"]].head(10))

print("\nMake year and reg year info:")
print(df_clean[["make_year", "reg_year"]].describe())



# Check invalid prices
invalid_prices = df_clean[df_clean["price"] <= 0]
print("Invalid prices:", len(invalid_prices))

# Check invalid car manufacturing years
invalid_years = df_clean[
    (df_clean["make_year"] < 1900) |
    (df_clean["make_year"] > 2026)
]
print("Invalid manufacturing years:", len(invalid_years))

# Check invalid mileage
invalid_mileage = df_clean[df_clean["km_driven"] < 0]
print("Invalid mileage:", len(invalid_mileage))

# Check invalid engine capacity
invalid_engine = df_clean[
    df_clean["engine_capacity(CC)"] <= 0
]
print("Invalid engine capacity:", len(invalid_engine))


#  Save cleaned data

df_clean.to_csv(
"data/used_cars_cleaned.csv",
index=False
)

print("\nCleaned data saved successfully!")

# Check the cleaned CSV file

df_check = pd.read_csv("data/used_cars_cleaned.csv")

# Show first 5 rows
print(df_check.head())

# Show rows and columns
print("\nDataset shape:")
print(df_check.shape)

# Check missing values
print("\nMissing values:")
print(df_check.isnull().sum())