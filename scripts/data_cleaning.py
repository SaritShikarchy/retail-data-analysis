import pandas as pd
import numpy as np
import os
import sqlite3

print("files in data folder:", os.listdir("../data"))
df= pd.read_csv("../data/online_retail_raw.csv", encoding="ISO-8859-1")
df.head()
df.info()
df= df[df["Quantity"]>0]
df= df.dropna (subset=["CustomerID"])
df["Revenue"]=df["Quantity"] * df["UnitPrice"]
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], dayfirst=True)
df["Year"]= df["InvoiceDate"].dt.year
df["Month"]= df["InvoiceDate"].dt.month
df["IsRepeatCustomer"] = np.where(df.groupby("CustomerID")["InvoiceNo"].transform("count") > 1, 1, 0)
df.head()
df.describe()
df.to_csv("../data/online_retail_clean.csv", index=False)
conn = sqlite3.connect("online_retail.db")
df.to_sql("sales", conn, if_exists="replace", index=False)

revenue_per_country_query  = """
SELECT Country, SUM(Revenue) as total_revenue
FROM sales
GROUP BY Country
ORDER BY total_revenue DESC"""
print("files in sql folder:", os.listdir("../sql"))
result1 = pd.read_sql(revenue_per_country_query , conn)
with open(r"..\sql\most_sales_products_query.sql", "r") as f:
    most_sales_products_query = f.read()
result2 = pd.read_sql(most_sales_products_query, conn)
print(result1.head())
print(result2.head())

