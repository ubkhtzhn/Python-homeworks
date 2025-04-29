# Homework 1:

import pandas as pd

# data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} 

# df = pd.DataFrame(data)

# df = df.rename(columns={'First Name' : 'first_name'})   # # # Rename column names
# df = df.rename(columns={'Age' : 'age'})                 # # # Rename column names

# mean_age = df['age'].mean()                             # # # Find the mean age of the individuals

# print(df)

# print(f"Mean age is {mean_age}")
# print(df.head(3))                                     # # # Print the first 3 rows of the DataFrame
# print(df[['First Name', 'City']])                     # # # Select and print only the 'Name' and 'City' columns


# salary =[4000, 1500, 2300, 3000]

# df['salary'] = salary                                 # # # Add a new column 'Salary' with random salary values


# print(df.describe())                                  # # # Display summary statistics of the DataFrame





# Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses',
#  representing monthly sales and expenses data. Use below table.


# # # Calculate and display the maximum sales and expenses.
# # # Calculate and display the minimum sales and expenses.
# # # Calculate and display the average sales and expenses.

# sales_and_expenses = {'Months': ['Jan', 'Feb', 'Mar', 'Apr'], 'Sales': [5000, 6000, 7500, 8000], 'Expenses': [3000, 3500, 4000, 4500]}


# df = pd.DataFrame(sales_and_expenses)

# maximum_sales = df['Sales'].max()
# maximum_expenses = df['Expenses'].max()
# minimum_sales = df['Sales'].min()
# minimum_expenses = df['Expenses'].min()
# average_sales = df['Sales'].mean()
# average_expenses = df['Expenses'].mean()


# print(f"Maximum sales is {maximum_sales},\nMinimum sales is {minimum_sales}.")
# print(f"Maximum expenses is {maximum_expenses}, \nMinimum expenses is {minimum_expenses}.")
# print(f"Average by sales is {average_sales}, \nAverage by expenses is {average_expenses}.")

# expenses = {'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'], 'January': [1200, 200, 300, 150], 'February' :[1300, 220, 320, 100], 'March': [1400,240,330, 170], 'April':[1500, 250, 350, 180]}

# df = pd.DataFrame(expenses)
# # print(df)
# expenses_indexed = df.set_index('Category')

# # print(df)
# print('Maximum by category')
# print(expenses_indexed.max(axis=1))
# print('Minimum by category ')
# print(expenses_indexed.min(axis=1))
# print('Average by category')
# print(expenses_indexed.mean(axis=1))
