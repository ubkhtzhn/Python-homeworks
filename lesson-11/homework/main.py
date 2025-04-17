############################## Exercise 1 ###########################

# python -m venv venv

# venv\Scripts\activate

# pip install requests flask

# pip list


############################ Exercise 2 ############################


import math_operations as mo
import string_utils as su


print(mo.add(10, 5))        
print(mo.subtract(10, 5))   
print(mo.multiply(10, 5))   
print(mo.divide(10, 0))   


print(su.reverse_string("hello")) 
print(su.count_vowels("hello"))    

############################ Exercise 3 ############################



from geometry.circle import calculate_area, calculate_circumference
from file_operations.file_reader import read_file
from file_operations.file_writer import write_file


r = 5
print(f"Area: {calculate_area(r):.2f}")
print(f"Circumference: {calculate_circumference(r):.2f}")


write_file("test.txt", "Hello, world!")
print("File content:", read_file("test.txt"))

