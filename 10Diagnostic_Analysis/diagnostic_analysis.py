# Country comparison and Pearson correlation
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

df = pd.read_csv("data.csv", encoding="ISO-8859-1")

# Convert columns to suitable data types
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")

# Remove rows missing fields needed for this analysis
df = df.dropna(subset=["InvoiceNo", "Country", "Quantity", "UnitPrice"])

# Keep completed purchase lines for this exercise
df = df[
    (df["Quantity"] > 0) &
    (df["UnitPrice"] >= 0) &
    (~df["InvoiceNo"].astype(str).str.startswith("C"))
].copy()

# Calculate line revenue
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

print("Rows available for analysis:", len(df))
country_summary = (
    df.groupby("Country")
    .agg(
        TotalRevenue=("Revenue", "sum"),
        OrderCount=("InvoiceNo", "nunique"),
        TotalQuantity=("Quantity", "sum")
    )
    .reset_index()
)

country_summary = country_summary.sort_values(
    "TotalRevenue", ascending=False
)

print(country_summary.head(10))
print("Number of countries:", len(country_summary))
plt.figure(figsize=(9, 5))
plt.scatter(
    country_summary["OrderCount"],
    country_summary["TotalRevenue"]
)
plt.xlabel("Number of Orders")
plt.ylabel("Total Revenue (GBP)")
plt.title("Country Orders vs Total Revenue")
plt.tight_layout()
plt.show()
