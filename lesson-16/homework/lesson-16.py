# # # 1. Convert List to 1D Array
# # # Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.

# # # Expected Output:

# # # Original List: [12.23, 13.32, 100, 36.32] One-dimensional NumPy array: [ 12.23 13.32 100. 36.32]


org_list = [12.23, 13.32, 100, 36.32]
np_list = np.array(org_list)

# # # 2. Create 3x3 Matrix (2?10)
# # # Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

# # # Expected Output:

# # # [[ 2 3 4] [ 5 6 7] [ 8 9 10]]

a = np.arange(2,11).reshape(3,3)


# # # 3. Null Vector (10) & Update Sixth Value
# # # Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.

# # # [ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

# # # Update sixth value to 11 [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]

null_vector = np.zeros(10)
null_vector[6] = 11

# # # 4. Array from 12 to 38
# # # Write a NumPy program to create an array with values ranging from 12 to 38.

# # # Expected Output:

# # # [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]

b = np.array(np.arange(12,38))


# # # 5. Convert Array to Float Type
# # # Write a NumPy program to convert an array to a floating type.

# # # Sample output:

# # # Original array [1, 2, 3, 4]

f_array = np.array([1,2,3,4])
after_array = np.array(f_array, dtype=float)
after_array

# # # 6. Celsius to Fahrenheit Conversion
# # # Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. Centigrade values are stored in a NumPy array.

# # # Sample Array [0, 12, 45.21, 34, 99.91] [-17.78, -11.11, 7.34, 1.11, 37.73, 0. ]

# # # Expected Output:

# # # Values in Fahrenheit degrees: [ 0. 12. 45.21 34. 99.91 32. ]

# # # Values in Centigrade degrees: [-17.78 -11.11 7.34 1.11 37.73 0. ]

centigrade = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])

fahrenheit = (centigrade*1.8) + 32
np.round(fahrenheit,2)

# # # 7. Append Values to Array (Do self-tudy)
# # # Write a NumPy program to append values to the end of an array.

# # # Expected Output:

# # # Original array: [10, 20, 30]

# # # After append values to the end of the array: [10 20 30 40 50 60 70 80 90]

c = np.array([10, 20, 30])
c = np.append(c, [40,50,60,70,80,90])


# # # 8. Array Statistical Functions (Do self-tudy)
# # # Create a random NumPy array of 10 elements and calculate the mean, median, and standard deviation of the array.

x = np.random.randn(10)
mean = np.mean(x)
median = np.median(x)
sd = np.std(x)
print(f"Mean is {mean}")
print(f"Median is {median}")
print(f"Standard deviation is {sd}")

# # # 9 Find min and max
# # # Create a 10x10 array with random values and find the minimum and maximum values.

x = np.random.randn(10, 10)
maximum = np.max(x)
minimum = np.min(x)
print(f"Maximum value is {maximum}")
print(f"Minimum value is {minimum}")

# # # 10
# # # Create a 3x3x3 array with random values.

y = np.random.randn(3, 3, 3)
print(y)
