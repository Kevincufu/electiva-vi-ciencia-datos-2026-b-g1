import pandas as pd

# ACTIVIDAD SEMANA 09 - Modelo, consulta y limpieza de datos
# Estudiante: Kevin Andres Cuevas Fuentes

df = pd.read_csv("sales_raw.csv")

print("BEFORE CLEANING")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("Missing values:", df.isna().sum().sum())
print("Duplicated rows:", df.duplicated().sum())

# Text cleaning
for col in ["customer_name", "email", "city", "product", "category", "status"]:
    df[col] = df[col].astype("string").str.strip()

df["city"] = df["city"].replace({"Bogota": "Bogotá"})
df["status"] = df["status"].str.lower().str.capitalize()

# Type correction
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
df["unit_price"] = (
    df["unit_price"].astype("string")
      .str.replace(",", "", regex=False)
      .str.replace(".", "", regex=False)
      .astype("Float64")
)
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce").astype("Int64")

# Missing values
df["email"] = df["email"].fillna("not_provided")
df["order_date"] = df["order_date"].fillna(df["order_date"].dropna().median())

# Duplicates and calculated field
df = df.drop_duplicates().reset_index(drop=True)
df["total_value"] = (df["unit_price"].astype(float) * df["quantity"].astype(float)).round(2)

print("\nAFTER CLEANING")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("Missing values:", df.isna().sum().sum())
print("Duplicated rows:", df.duplicated().sum())

df.to_csv("sales_clean.csv", index=False)

# QUERY 1
q1 = (df[df["status"] == "Completed"]
      .groupby("category")["total_value"]
      .sum()
      .sort_values(ascending=False))
print("\nQUERY 1 - Completed sales by category")
print(q1)

# QUERY 2
q2 = (df[df["status"] == "Completed"]
      .groupby("city")["total_value"]
      .sum()
      .sort_values(ascending=False)
      .head(5))
print("\nQUERY 2 - Top 5 cities by completed sales")
print(q2)
