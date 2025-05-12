import pandas as pd
import numpy as np

df = pd.read_csv('sales_data.csv')

# # # 1. Group the data by the Category column and calculate the following aggregate statistics for each category:
# # # Total quantity sold.
# # # Average price per unit.
# # # Maximum quantity sold in a single transaction.



df.groupby('Category')['Quantity'].sum()
df.groupby('Category')['Price'].mean()
df.groupby('Category')['Quantity'].max()


# # # 2. Identify the top-selling product in each category based on the total quantity sold.

top_selling = df.loc[df.groupby('Category')['Quantity'].idxmax()]
top_selling[['Product', 'Quantity']]


# # # 3. Find the date on which the highest total sales (quantity * price) occurred.

df['Total'] = df['Price']*df['Quantity']

highest_sale_date = df.loc[df['Total'].idxmax(), 'Date']
highest_sale_date

# # # 1. Group the data by CustomerID and filter out customers who have made less than 20 orders.

customer_df = pd.read_csv('customer_orders.csv')
customer_quantity = customer_df.groupby('CustomerID')['Quantity'].sum()
customer_less_20 = customer_quantity[customer_quantity < 20]
customer_less_20

# # # 2. Identify customers who have ordered products with an average price per unit greater than $120.

customer_avg = customer_df.groupby('CustomerID')['Price'].mean()
customer_avg[customer_avg > 120]

# # # 3. Find the total quantity and total price for each product ordered, and filter out products that have a total quantity less than 5 units.

customer_df['Total'] = customer_df['Price']*customer_df['Quantity']
total_quantity_price = customer_df.groupby('Product')[['Quantity', 'Total']].sum()
less_5 = total_quantity_price[total_quantity_price['Quantity']<5]
less_5



