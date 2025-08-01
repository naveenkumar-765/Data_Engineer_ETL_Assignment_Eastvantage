import sqlite3
import csv

# Connecting to the sqlite database
conn = sqlite3.connect('Data_Engineer_ETL_Assignment.db')
cursor = conn.cursor()


# SQL Query
query = """
select c.customer_id as Customer, c.age as Age, i.item_name as Item, SUM(o.quantity) as Quantity
from Customers c
join Sales s on c.customer_id = s.customer_id
join Orders o on s.sales_id = o.sales_id
join Items i on o.item_id = i.item_id
where c.age between 18 and 35 and o.quantity is NOT NULL
group by c.customer_id, c.age, i.item_name
having SUM(o.quantity) > 0
order by c.customer_id;
"""

cursor.execute(query)
results = cursor.fetchall() # fetching the results and storing like a tuple

# writing to a csv file with ; delimiter
with open('results_sql.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(['Customer', 'Age', 'Item', 'Quantity'])
    for row in results:
        writer.writerow([row[0], row[1], row[2], int(row[3])])  # No decimals

conn.close()