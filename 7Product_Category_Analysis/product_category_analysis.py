# Product and category analysis
import pandas as pd
import matplotlib.pyplot as plt
# Make sure quantity and price are numeric
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")
df = df.dropna(subset=["StockCode", "Product", "Category",
                       "Quantity", "UnitPrice"])
df = df[df["UnitPrice"] > 0]
print("Rows available for analysis:", len(df))
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

print(df[["Product", "Quantity", "UnitPrice", "Revenue"]].head())
product_summary = df.groupby(
    ["StockCode", "Product"], as_index=False
).agg(
    Total_Quantity=("Quantity", "sum"),
    Total_Revenue=("Revenue", "sum")
)
product_summary = product_summary.sort_values(
    by="Total_Revenue", ascending=False
)
print(product_summary.head(10))
category_summary = df.groupby(
    "Category", as_index=False
).agg(
    Total_Quantity=("Quantity", "sum"),
    Total_Revenue=("Revenue", "sum")
)

category_summary = category_summary.sort_values(
    by="Total_Revenue", ascending=False
)

print(category_summary)
plt.figure(figsize=(10, 5))
plt.bar(top_products["Product"], top_products["Total_Revenue"])
plt.title("Top 10 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Net Revenue")
plt.xticks(rotation=75, ha="right")
plt.tight_layout()
plt.show()
plt.figure(figsize=(9, 5))
plt.bar(category_summary["Category"], category_summary["Total_Revenue"])
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Net Revenue")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
plt.figure(figsize=(9, 5))
plt.bar(category_summary["Category"], category_summary["Total_Quantity"])
plt.title("Quantity Sold by Category")
plt.xlabel("Category")
plt.ylabel("Net Quantity")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
volume_products.plot(
    x="Product",
    y=["Quantity_Percent", "Revenue_Percent"],
    kind="bar",
    figsize=(11, 5)
)

plt.title("Product Volume Share vs Revenue Share")
plt.xlabel("Product")
plt.ylabel("Share of Total (%)")
plt.xticks(rotation=75, ha="right")
plt.tight_layout()
plt.show()
