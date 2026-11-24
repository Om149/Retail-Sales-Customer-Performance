# Data cleaning and preprocessing
import pandas as pd
import numpy as np
import os
df_raw = pd.read_csv("data.csv", encoding="ISO-8859-1")
df = df_raw.copy()
print("Raw dataset loaded")
print("Original shape:", df_raw.shape)
baseline = {
    "rows": len(df),
    "columns": len(df.columns),
    "missing_cells": int(df.isna().sum().sum()),
    "exact_duplicates": int(df.duplicated().sum()),
    "quantity_sum_raw": pd.to_numeric(df["Quantity"], errors="coerce").sum(),
    "unit_price_sum_raw": pd.to_numeric(df["UnitPrice"], errors="coerce").sum()
}
print("BEFORE CLEANING")
print(baseline)
df.columns = df.columns.str.strip()
for column in ["InvoiceNo", "StockCode", "Description", "Country"]:
    df[column] = df[column].astype("string").str.strip()
print("Country values:")
print(sorted(df["Country"].dropna().unique().tolist())[:5])
df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"], errors="coerce"
)
df["Quantity"] = pd.to_numeric(
    df["Quantity"], errors="coerce"
)
df["UnitPrice"] = pd.to_numeric(
    df["UnitPrice"], errors="coerce"
)
df["CustomerID"] = df["CustomerID"].astype("string").str.strip()
print(df.dtypes)
print("Missing values by column:")
print(df.isna().sum())
duplicates_before = int(df.duplicated().sum())
df = df.drop_duplicates().copy()
duplicates_removed = duplicates_before - int(df.duplicated().sum())
print("Duplicates found:", duplicates_before)
print("Duplicates removed:", duplicates_removed)
print("Rows after removal:", len(df))
df["flag_missing_customer"] = df["CustomerID"].isna()
df["flag_missing_description"] = df["Description"].isna()
df["flag_invalid_date"] = df["InvoiceDate"].isna()
df["flag_missing_quantity"] = df["Quantity"].isna()
df["flag_missing_price"] = df["UnitPrice"].isna()
df["flag_cancellation_invoice"] = df["InvoiceNo"].str.startswith("C", na=False)
df["flag_nonpositive_quantity"] = df["Quantity"].le(0)
df["flag_nonpositive_price"] = df["UnitPrice"].le(0)
print("Quality flags created")
