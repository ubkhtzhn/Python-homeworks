# Exercise 1 #
# Given a side of square. Find its perimeter and area.

a = 5          # side of square
P = 4*a        # perimetr of square
S = a**2       # area of square
print(f"Perimetr of square: {P}\nArea of square: {S}")

# Exercise 2 #
# Given diameter of circle. Find its length.

import math
d = 6            # diameter of circle
l = math.pi * d  # length of circle

print(f"Length of circle: {l}")

# Exercise 3 #
# Given two numbers a and b. Find their mean.

a = 4
b = 8
m = (a+b)/2

print(f"Mean of {a} and {b} is {m}")

# Exercise 4 #
# Given two numbers a and b. Find their sum, product and square of each number.

a = 4
b = 6
sum = a+b
product = a*b
asquare = a**2
bsquare = b**2
print(f"Sum of {a} and {b} is {sum}.\nProduct of {a} and {b} is {product}.\nSquare of {a} is {asquare} and square of {b} is {bsquare}")
