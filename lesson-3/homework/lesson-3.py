# # # 1. Create and Access List Elements
# # # Create a list containing five different fruits and print the third fruit.

fruitsgo = ['pear', 'apple', 'banana', 'lemon', 'grapes']
print(fruitsgo[2])        # printing the third element of list

# # # 2. Concatenate Two Lists
# # # Create two lists of numbers and concatenate them into a single list.

fruits = ['pear', 'apple', 'banana', 'lemon', 'grapes']
vegetables = ['carrot', 'tomato', 'onion', 'potato', 'cucumber']
fruits_and_vegetables = fruits[:] + vegetables[:]     # concatenating two lists
print(fruits_and_vegetables)

# 3. Extract Elements from a List
# Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
import math
numbersshe = [1, 5, 10, 15, 20, 25, 30, 35, 40]
lengo = math.floor(len(numbersshe)/2)        # calculation of middle number
numbers1go = [numbersshe[0], numbersshe[lengo], numbersshe[-1]]
print(numbers1go)

# 4. Convert List to Tuple
# Create a list of your five favorite movies and convert it into a tuple.

movies = ['The Godfather', 'The Shawshank Redemption', 'Forrest Gump', 'The Matrix', 'Seven Samurai']  # creating list of movies
t_movies = tuple(movies)     #converting list to tuple                                                                          
print(t_movies) 

# # # 5. Check Element in a List
# # # Given a list of cities, check if "Paris" is in the list and print the result.

cities = ['Manchester', 'London', 'Paris', 'Moscow', 'Madrid']

if 'Paris' in cities:
    print('Yes, Paris is on the list.')
else:
    print('No, Paris is not on the list.')

# # # 6. Duplicate a List Without Using Loops
# # # Create a list of numbers and duplicate it without using loops.

numbersgoy = [1, 3, 5, 7, 9]
copy_numbers = numbersgoy[:]

print(numbersgoy)
print(copy_numbers)

# # # 7. Swap First and Last Elements of a List
# # # Given a list of numbers, swap the first and last elements.

numbers = [1, 3, 5, 7, 9, 11]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)

# # # 8. Slice a Tuple
# # # Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

tuple_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tuple_numbers[3:7])

# 9. Count Occurrences in a List
# Create a list of colors and count how many times "blue" appears in the list.

colors = ['yellow', 'red', 'blue', 'green', 'pink', 'blue']
print(f'The blue appears in this list {colors.count('blue')} times')

# 10. Find the Index of an Element in a Tuple
# Given a tuple of animals, find the index of "lion".

animals = ['lion', 'tiger', 'bear', 'crocodile', 'giraffe', 'dear']
print(f"The lions' index number is {animals.index('lion')}")

# # # 11. Merge Two Tuples
# # # Create two tuples of numbers and merge them into a single tuple.

numbersgo = (1, 3, 5, 7, 9)
numbersgo1 = (2, 4, 6, 8, 10)
merge_num = numbersgo[:] + numbersgo1[:]
print(merge_num)

# # # 12. Find the Length of a List and Tuple
# # # Given a list and a tuple, find and print their lengths.

listgo = [1, 3, 5, 7, 9]
tuplego = (2, 4, 6, 8, 10, 12)
print(f'The length of list is {len(listgo)}')
print(f'The length of tuple is {len(tuplego)}')

# # # 13. Convert Tuple to List
# # # Create a tuple of five numbers and convert it into a list.

tup_num = (1, 3, 5, 7, 9)
list_num = list(tup_num)
print(list_num)

# # # 14. Find Maximum and Minimum in a Tuple
# # # Given a tuple of numbers, find and print the maximum and minimum values.

tup_numgo = [1, 3, 5, 7, 9, 11, 23]
maxgo = max(tup_numgo)
mingo = min(tup_numgo)
print(f'Maximum number in this tuple is {maxgo} and minimum is {mingo}')

# # # 15. Reverse a Tuple
# # # Create a tuple of words and print it in reverse order.

tuple_words = ('jay', 'jer', 'soz', 'bala')
reverse_tup = tuple_words[::-1]
print(reverse_tup)
