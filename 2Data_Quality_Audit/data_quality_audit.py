# Data-quality audit
import pandas as pd
df = pd.read_csv(
    "01_raw/online_retail_raw.csv",
    encoding="ISO-8859-1"
)
print("Audit dataset loaded")
rows, columns = df.shape
print("Total records:", rows)
print("Total columns:", columns)
print("Column names:", df.columns.tolist())
missing_count = df.isnull().sum()
missing_percent = (missing_count / len(df)) * 100
missing_report = pd.DataFrame({
    "Missing Count": missing_count,
    "Missing Percentage": missing_percent.round(2)
})
print(missing_report)
duplicate_count = df.duplicated().sum()
print("Exact duplicate rows:", duplicate_count)
duplicate_rows = df[df.duplicated(keep=False)]
print(duplicate_rows.head(10))
df["InvoiceDate_parsed"] = pd.to_datetime(
    df["InvoiceDate"],
    errors="coerce"
)
invalid_dates = df["InvoiceDate_parsed"].isna().sum()
print("Invalid or unparsed dates:", invalid_dates)
print(df[ df["InvoiceDate_parsed"].isna() ][["InvoiceDate"]].head())
print(df.dtypes)
print("Quantity type:", df["Quantity"].dtype)
print("UnitPrice type:", df["UnitPrice"].dtype)
print("InvoiceDate source type:", df["InvoiceDate"].dtype)
print("Negative quantities:",
      (df["Quantity"] < 0).sum())
print("Zero quantities:",
      (df["Quantity"] == 0).sum())
print(df[df["Quantity"] <= 0][
    ["InvoiceNo", "StockCode", "Quantity", "InvoiceDate"]
].head(10))
print("Negative unit prices:",
      (df["UnitPrice"] < 0).sum())
print("Zero unit prices:",
      (df["UnitPrice"] == 0).sum())
print(df[df["UnitPrice"] <= 0][
    ["InvoiceNo", "StockCode", "Description", "UnitPrice"]
].head(10))
print(df[["Quantity", "UnitPrice"]].describe())
print("Highest quantities:")
print(df.nlargest(10, "Quantity")[
    ["InvoiceNo", "StockCode", "Quantity", "UnitPrice"]
])
print("Highest unit prices:")
print(df.nlargest(10, "UnitPrice")[
    ["InvoiceNo", "StockCode", "Quantity", "UnitPrice"]
])
invoice_text = df["InvoiceNo"].astype("string")
cancellation_count = invoice_text.str.startswith(
    "C", na=False
).sum()
print("Invoices / rows with C-prefixed invoice number:",
      cancellation_count)
print(df[invoice_text.str.startswith("C", na=False)][
    ["InvoiceNo", "Quantity", "UnitPrice"]
].head(10))
df["InvoiceDate_parsed"] = pd.to_datetime(
    df["InvoiceDate"],
    errors="coerce"
)
invoice_text = df["InvoiceNo"].astype("string")
audit_summary = pd.DataFrame({
    "Issue": [
        "Missing values",
        "Exact duplicate rows",
        "Invalid dates",
        "Negative quantities",
        "Zero quantities",
        "Negative unit prices",
        "Zero unit prices",
        "C-prefixed invoice rows"
    ],
    "Count": [
        int(df.isnull().sum().sum()),
        int(df.duplicated().sum()),
        int(df["InvoiceDate_parsed"].isna().sum()),
        int((df["Quantity"] < 0).sum()),
        int((df["Quantity"] == 0).sum()),
        int((df["UnitPrice"] < 0).sum()),
        int((df["UnitPrice"] == 0).sum()),
        int(invoice_text.str.startswith("C", na=False).sum())
    ]
})
print(audit_summary)
audit_summary.to_csv(
    "04_outputs/day18_audit_summary.csv",
    index=False
)
missing_report.to_csv(
    "04_outputs/day18_missing_values.csv"
)
print("Audit reports saved")
