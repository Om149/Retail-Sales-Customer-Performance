# Extracted from Day16-30(1).docx. Source code text is retained as documented.
# Dataset loading and inspection
import pandas as pd
file_path = "01_raw/online_retail_raw.csv"
df = pd.read_csv(
    file_path,
    encoding="ISO-8859-1"
)
print("Dataset loaded successfully")
print(df.head())
print("Rows and columns:", df.shape)
print(df.columns.tolist())
df.info()
print(df.isnull().sum())
print(df.describe(include="all"))
df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"],
    errors="coerce"
)
print("Earliest date:", df["InvoiceDate"].min())
print("Latest date:", df["InvoiceDate"].max())
