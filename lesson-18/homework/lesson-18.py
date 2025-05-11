# # # 1. Find all questions that were created before 2014

import pandas as pd
import numpy as np

df = pd.read_csv('tackoverflow_qa.csv')
df['creationdate'] = pd.to_datetime(df['creationdate'])
df_before2014 = df[df['creationdate']< '2014-01-01']
df_before2014

# # # 2. Find all questions with a score more than 50

df_score_more_50 = df[df['score']>50]

df_score_more_50


# # # 3. Find all questions with a score between 50 and 100

df_score_between_50_100 = df[(df['score']>50) & (df['score']<100)]
df_score_between_50_100

# # # 4. Find all questions answered by Scott Boston

df_scott_boston = df[df['ans_name'] == 'Scott Boston']
df_scott_boston

# # # 5. Find all questions answered by the following 5 users

df.head(5)

# # # 6. Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.


df['creationdate'] = pd.to_datetime(df['creationdate'])
between_mar_oct = df[(df['creationdate'] < '2014-10-01') & (df['creationdate'] > '2014-03-01')]
ans_unutbu = between_mar_oct[between_mar_oct['ans_name'] == 'Unutbu']
less_than_5 = ans_unutbu[ans_unutbu['score'] < 5]
less_than_5


# # # 7. Find all questions that have score between 5 and 10 or have a view count of greater than 10,000

df_5_10 = df[(df['score'] > 5) & (df['score'] < 10) & (df['viewcount'] > 10000)]
df_5_10


# # # 8. Find all questions that are not answered by Scott Boston

not_boston = df[df['ans_name'] != 'Scott Boston']
not_boston

# # # 1. Select Female Passengers in Class 1 with Ages between 20 and 30: 
# # # Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30.

titanic_df = pd.read_csv('titanic.csv')
female_20_30 = titanic_df[(titanic_df['Sex'] == 'female') & (titanic_df['Pclass'] == 1) & (titanic_df['Age'] > 20) & (titanic_df['Age'] < 30)]
female_20_30


# # # 2. Filter Passengers Who Paid More than $100: Create a DataFrame with passengers who paid a fare greater than $100.

more_100 = titanic_df[(titanic_df['Fare']>100)]
more_100

# # # 3. Select Passengers Who Survived and Were Alone: Filter passengers who survived and 
# # # were traveling alone (no siblings, spouses, parents, or children).

alone_survived = titanic_df[(titanic_df['Survived'] == 1) & (titanic_df['SibSp'] == 0) & (titanic_df['Parch'] == 0)]
alone_survived

# # # 4. Filter Passengers Embarked from 'C' and Paid More Than $50: Create a DataFrame with passengers who embarked from 'C' and 
# # # paid more than $50.

more_50_c = titanic_df[(titanic_df['Embarked'] == 'C') & (titanic_df['Fare'] > 50)]

more_50_c

# # # 5. Select Passengers with Siblings or Spouses and Parents or Children: Extract passengers who had 
# # # both siblings or spouses aboard and parents or children aboard.

not_alone = titanic_df[(titanic_df['SibSp'] == 1) & (titanic_df['Parch'] == 1)]
not_alone


# # # 6. Filter Passengers Aged 15 or Younger Who Didn't Survive: Create a DataFrame with passengers aged 15 or younger who did not survive.

less_15_not_survived = titanic_df[(titanic_df['Survived'] == 0) & (titanic_df['Age'] <= 15)]
less_15_not_survived

# # # 7. Select Passengers with Cabins and Fare Greater Than $200: Extract passengers with known cabin numbers and a fare greater than $200.

greater_200 = titanic_df[(titanic_df['Fare'] > 200) & (titanic_df['Cabin'].notna())]

greater_200

# # # 8. Filter Passengers with Odd-Numbered Passenger IDs: Create a DataFrame with passengers whose PassengerId is an odd number.

odd_id = titanic_df[(titanic_df['PassengerId'] % 2 == 1)]
odd_id

# # # 9. Select Passengers with Unique Ticket Numbers: Extract a DataFrame with passengers having unique ticket numbers.

unique_tickets = titanic_df[~titanic_df['Ticket'].duplicated(keep=False)]

unique_tickets

# # # 10. Filter Passengers with 'Miss' in Their Name and Were in Class 1: Create a DataFrame with female 
# # # passengers having 'Miss' in their name and were in Class 1.

class_1_miss = titanic_df[(titanic_df['Pclass'] == 1) & (titanic_df['Name'].str.contains('Miss', case = False, na= False))]
class_1_miss


