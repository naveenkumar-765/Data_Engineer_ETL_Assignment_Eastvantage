import sqlite3
import pandas as pd

# database connection
conn = sqlite3.connect('Data_Engineer_ETL_Assignment.db')

# Loading tables into pandas
customers_df = pd.read_sql_query("select * from Customers", conn)
sales_df = pd.read_sql_query("select * from Sales", conn)
orders_df = pd.read_sql_query("select * from Orders", conn)
items_df = pd.read_sql_query("select * from Items", conn)

# Merging all tables
merged_df = orders_df.merge(sales_df, on='sales_id').merge(customers_df, on='customer_id').merge(items_df, on='item_id')

# Filtering by age and quantities
filtered_df = merged_df[(merged_df['age'].between(18, 35)) & (merged_df['quantity'].notnull()) & (merged_df['quantity'] > 0)]

# Grouping and sum
grouped_df = filtered_df.groupby(['customer_id', 'age', 'item_name'])['quantity'].sum().reset_index()

# Rename and reorder
grouped_df.columns = ['Customer', 'Age', 'Item', 'Quantity']
grouped_df['Quantity'] = grouped_df['Quantity'].astype(int)

# Saving to CSV
grouped_df.to_csv('results_pandas.csv', sep=';', index=False)

conn.close()