# KPI and feature calculations
import pandas as pd
import os
sales = pd.read_csv(
    "04_outputs/day20_analysis_ready_sales.csv",
    encoding="ISO-8859-1",
    parse_dates=["InvoiceDate"]
)
print("Analysis-ready sales data loaded")
print(sales.head())
print(sales.shape)
sales["Revenue"] = sales["Quantity"] * sales["UnitPrice"]
print(sales[["InvoiceNo", "StockCode", "Quantity", "UnitPrice", "Revenue"]].head())
total_revenue = sales["Revenue"].sum()
print("Total Revenue (GBP):", round(total_revenue, 2))
total_orders = sales["InvoiceNo"].nunique()
print("Total Orders:", total_orders)
average_order_value = total_revenue / total_orders if total_orders > 0 else 0
print("Average Order Value (GBP):", round(average_order_value, 2))
total_units_sold = sales["Quantity"].sum()
print("Total Units Sold:", int(total_units_sold))
revenue_by_product = (
    sales.groupby(["StockCode", "Description"], dropna=False)["Revenue"]
    .sum()
    .reset_index()
    .sort_values("Revenue", ascending=False)
)
print(revenue_by_product.head(10))
revenue_by_country = (
    sales.groupby("Country")["Revenue"]
    .sum()
    .reset_index()
    .sort_values("Revenue", ascending=False)
)
print(revenue_by_country.head(10))
kpi_summary = pd.DataFrame({
    "KPI": [
        "Total Revenue (GBP)",
        "Number of Orders",
        "Average Order Value (GBP)",
        "Total Units Sold"
    ],
    "Value": [
        round(total_revenue, 2),
        int(total_orders),
        round(average_order_value, 2),
        int(total_units_sold)
    ]
})
print(kpi_summary)
