# Monthly sales trend analysis
import pandas as pd
import matplotlib.pyplot as plt
# Load the cleaned dataset
df = pd.read_csv("sales_cleaned.csv")
# Convert OrderDate into a date format
df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")
# Remove rows that do not have a valid date or revenue
df = df.dropna(subset=["OrderDate", "Revenue"])
# Make sure Revenue is numeric
df["Revenue"] = pd.to_numeric(df["Revenue"], errors="coerce")
df = df.dropna(subset=["Revenue"])
print(df.head())
print(df[["OrderDate", "Revenue"]].info())
# Create a month column
df["Month"] = df["OrderDate"].dt.to_period("M").astype(str)
# Calculate monthly revenue
monthly_revenue = df.groupby("Month")["Revenue"].sum()
# Calculate monthly order count
monthly_orders = df.groupby("Month")["OrderID"].nunique()
# Combine the results into one table
monthly_summary = pd.DataFrame({
    "Revenue": monthly_revenue,
    "Order_Count": monthly_orders
})
print(monthly_summary)
plt.figure(figsize=(10, 5))
plt.plot(monthly_summary.index, monthly_summary["Revenue"], marker="o")
plt.title("Monthly Sales Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
highest_month = monthly_summary["Revenue"].idxmax()
lowest_month = monthly_summary["Revenue"].idxmin()
print("Highest revenue month:", highest_month)
print("Highest revenue:", monthly_summary["Revenue"].max())
print("Lowest revenue month:", lowest_month)
print("Lowest revenue:", monthly_summary["Revenue"].min())
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("cleaned_data.csv", encoding="ISO-8859-1")
df["OrderID"] = df["InvoiceNo"]
df["Category"] = df["Description"]
df["OrderDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")
df["Revenue"] = (
    pd.to_numeric(df["Quantity"], errors="coerce") *
    pd.to_numeric(df["UnitPrice"], errors="coerce")
)
df = df.dropna(subset=["OrderDate", "Revenue", "OrderID"])
df["Month"] = df["OrderDate"].dt.to_period("M").astype(str)
monthly_summary = df.groupby("Month").agg(
    Revenue=("Revenue", "sum"),
    Order_Count=("OrderID", "nunique")
)
print(monthly_summary)
fig, ax1 = plt.subplots(figsize=(12, 5))
ax1.plot(
    monthly_summary.index,
    monthly_summary["Revenue"],
    marker="o",
    label="Monthly Revenue"
)
ax1.set_xlabel("Month")
ax1.set_ylabel("Revenue")
ax1.tick_params(axis="x", rotation=45)
ax2 = ax1.twinx()
ax2.plot(
    monthly_summary.index,
    monthly_summary["Order_Count"],
    marker="s",
    linestyle="--",
    label="Monthly Order Count"
)
ax2.set_ylabel("Number of Orders")
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")
plt.title("Monthly Revenue vs Monthly Order Count")
plt.tight_layout()
plt.show()
