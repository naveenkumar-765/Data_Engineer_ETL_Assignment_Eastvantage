# Data_Engineer_ETL_Assignment_Eastvantage
A data analysis assignment using SQLite, SQL, and Python (Pandas) to extract and export customer purchase data.


# Customer Purchase Analysis – SQL & Python Assignment
This project analyzes customer item purchases from a sales database using both SQL and Python (Pandas). The goal is to extract item-wise quantities purchased by customers aged 18 to 35 and output the results in a semicolon-delimited CSV format.

# Problem Statement:
Company XYZ wants to analyze purchases made during a large promotional event. They are particularly interested in:
- Customers aged (18–35)
- Quantities of items purchased per customer

We have SQLite database file - 'Data_Engineer_ETL_Assignment.db' with 4 tables:  
- Customers(customer_id, age)
- Sales(sales_id, customer_id)
- Orders(order_id, sales_id, item_id, quantity)
- Items(item_id, item_name)

# Output Requirements
- Extract:
  - Each customer (age 18–35)
  - Each item purchased by them
  - Total quantity of each item
  - Rows with `quantity = NULL` or `0`
  - Output:
    A csv file with the below columns:  
    (Customer;Age;Item;Quantity) and delimiter is ';'


# Files Included
1. Data_Engineer_ETL_Assignment.db - Database file consists of all schema
2. using_sql - Python + SQL code
3. using_pandas - Python + Pandas
4. results_sql - Result data for the assignment
5. results_pandas - Result data for the assignment
