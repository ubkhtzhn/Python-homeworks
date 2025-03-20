# # # 1. Sort a Dictionary by Value
# # # Write a Python script to sort (ascending and descending) a dictionary by value.

biblioteka = {'football player': 'Messi', 'actor': 'Di Caprio', 'basketball player' : 'Jordan', 'tennis player': 'Roger Federer', 'singer': 'Morgenshtern'}
sorted_by_values_asc = sorted(biblioteka.values())
sorted_by_values_desc = sorted(biblioteka.values(), reverse=True)

print(sorted_by_values_asc)
print(sorted_by_values_desc)

# # # 2. Add a Key to a Dictionary
# # # Write a Python script to add a key to a dictionary.

bibl = {0:10, 1:20}
bibl[2] = 30

print(bibl)


# # # 3. Concatenate Multiple Dictionaries
# # # Write a Python script to concatenate the following dictionaries to create a new one.

a = {0:10, 1:20, 2:30}
b = {3:40, 4:50, 5:60}
combine_a_b = {}

for d in a,b:
    combine_a_b.update(d)

print(combine_a_b)

# # # 4. Generate a Dictionary with Squares
# # # Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

squares = {}
n = int(input('Enter the number: '))
for k in range(1, n+1):
    squares[k] = k**2
print(squares)

# # # 5. Dictionary of Squares (1 to 15)
# # # Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

squares2 = {}
for m in range(1, 16):
    squares2[m] = m**2
print(squares2)

# # # 1. Create a Set
# # # Write a Python program to create a set.

my_set = set()
print(my_set)

# # # 2. Iterate Over a Set
# # # Write a Python program to iterate over sets.

x = {1, 2, 3, 4, 5}
y = {3, 4, 5, 6, 7}

print(x & y) # Intersection
print(x | y) # Union
print(x - y) # Difference

# # # 3. Add Member(s) to a Set
# # # Write a Python program to add member(s) to a set.

my_set2 = {1, 2, 3}
my_set2.add(4)  # adding 1 element
print(my_set2)  # adding 1 element
my_set2.update([5,6,7])  # adding multiple elements
print(my_set2)

# # # 4. Remove Item(s) from a Set
# # # Write a Python program to remove item(s) from a given set.

z = {1, 2, 3, 4, 5}
print(z)

z.discard(1)  # without error if element not found
print(z)

z.clear()  # removes all elements
print(z)

# # # 5. Remove an Item if Present in the Set
# # # Write a Python program to remove an item from a set if it is present in the set.

p = {1, 2, 3, 4, 5}

p.remove(3)  # raising error if element not found
print(p)
