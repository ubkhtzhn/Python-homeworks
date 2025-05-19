import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

df1

# # # Exercise 1: Calculate the average grade for each student.

df1['Average_grade'] = df1[['Math', 'English', 'Science']].mean(axis=1)

df1


# # # Exercise 2: Find the student with the highest average grade.

df1_sorted = df1.sort_values(by='Average_grade', ascending=False)

df1_sorted.head(1)

# # # Exercise 3: Create a new column 'Total' representing the total marks obtained by each student.

df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis=1)

df1


# # # Exercise 4: Plot a bar chart to visualize the average grades in each subject.
import matplotlib.pyplot as plt

average_subjects = df1[['Math', 'English', 'Science']].mean()

plt.figure(figsize=(8, 5))
average_subjects.plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon'])

plt.title('Average Grades by Subject')
plt.ylabel('Average Grade')
plt.xlabel('Subject')
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)

for i, value in enumerate(average_subjects):
    plt.text(i, value + 1, f'{value:.1f}', ha='center', fontsize=10)

plt.tight_layout()
plt.show()


import pandas as pd

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

# # # Exercise 1: Calculate the total sales for each product.
totals = df2[['Product_A', 'Product_B', 'Product_C']].sum()
totals['Date'] = 'Total'

df2.loc['Total'] = totals

df2

# # # Exercise 2: Find the date with the highest total sales.

df2['Total'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)

max_ind = df2['Total'].idxmax()

highest = df2.loc[max_ind, 'Date']

print("Date with highest total sales:", highest)

