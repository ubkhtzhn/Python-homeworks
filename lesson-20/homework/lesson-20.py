# # # Find the total amount spent by each customer on purchases (considering invoices).

import pandas as pd
import numpy as np

import sqlite3


from sqlalchemy import create_engine

engine = create_engine('sqlite:///chinook.db')

engine

customers = pd.read_sql_table('customers', engine)

invoices = pd.read_sql_table('invoices', engine)

customer_spending = invoices.groupby('CustomerId')['Total'].sum().reset_index()

result = customer_spending.merge(customers[['CustomerId', 'FirstName', 'LastName']], on = 'CustomerId')

result = result[['CustomerId', 'FirstName', 'LastName', 'Total']]

result = result.sort_values(by='Total', ascending=False)

result

# # # Identify the top 5 customers with the highest total purchase amounts.


result.head(5)



# # # Display the customer ID, name, and the total amount spent for the top 5 customers.

result = result[['CustomerId', 'FirstName', 'Total']]

result = result.sort_values(by='Total', ascending=False)

result.head(5)


