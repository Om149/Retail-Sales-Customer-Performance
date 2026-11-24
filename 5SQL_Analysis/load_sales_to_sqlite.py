# SQLite data loading
import pandas as pd
import sqlite3
# Read the cleaned dataset
df = pd.read_csv("sales_cleaned.csv")
# Convert the order date to a date value
df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")
# Create or connect to the SQLite database
connection = sqlite3.connect("retail_sales.db")
# Load the data into a SQL table
df.to_sql("sales", connection, if_exists="replace", index=False)
print("Data loaded successfully.")
print("Number of rows:", len(df))
connection.close()
