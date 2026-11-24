# Pandas dashboard validation
import pandas as pd
# Step 1: Load cleaned dataset
df = pd.read_csv(
"cleaned_sales_data_updated.csv",
encoding="utf-8-sig"
)
# Step 2: Convert columns into correct data types
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Revenue"] = pd.to_numeric(df["Revenue"], errors="coerce")
df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")
df["InvoiceDate"] = pd.to_datetime(
df["InvoiceDate"], errors="coerce"
)
df["OrderDate"] = pd.to_datetime(
df["OrderDate"], errors="coerce"
)
# Step 3: Calculate Total Orders
total_orders = df["InvoiceNo"].nunique()
# Step 4: Calculate Total Quantity
total_quantity = df["Quantity"].sum()
# Step 5: Calculate Total Revenue
total_revenue = df["Revenue"].sum()
# Step 6: Calculate Average Order Value
average_order_value = (
total_revenue / total_orders
if total_orders != 0 else 0
)
# Step 7: Display validation results
print("===== POWER BI DASHBOARD VALIDATION =====")
print("Total Orders:", total_orders)
print("Total Quantity:", total_quantity)
print("Total Revenue:", round(total_revenue, 2))
print("Average Order Value:", round(average_order_value, 2))
