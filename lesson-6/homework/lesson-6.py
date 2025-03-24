# # # 1. Modify String with Underscores

def modify_string(txt):
    vowels = "aeiou"
    result = []
    count = 0  

    i = 0
    while i < len(txt):
        result.append(txt[i])
        if txt[i] not in vowels and (count + 1) % 3 == 0:
            if i + 1 < len(txt) and txt[i + 1] != "_": 
                result.append("_")
        count += 1
        i += 1

    return "".join(result)


# # # 2. Integer Squares Exercise
# # # Task
# # # The provided code stub reads an integer, n, from STDIN. For all non-negative integers i where 0 <= i < n, print i^2.

n = int(input('Enter the integer: '))
n_list = list(range(0, n))

for i in n_list:
    print(i**2)

# # # 3. Loop-Based Exercises
# # # Exercise 1: Print first 10 natural numbers using a while loop
# # # Exercise 2: Print the following pattern

n = 1
while n<=10:
    print(n)
    n+=1

n = 1

for b in range(5):  
    for i in range(1, n + 1):
        print(i, end=" ")
    print()  
    n += 1


# # Exercise 3: Calculate sum of all numbers from 1 to a given number

n = int(input('Enter the number: '))

sumgo = ((1+n)/2)*n
print(sumgo)

# # Exercise 4: Print multiplication table of a given number

n = int(input("Enter the number: "))
a = 1
while a <=10:
    print(a*n)
    a+=1

# # Exercise 5: Display numbers from a list using a loop

numbers = [12, 75, 150, 180, 145, 525, 50]

numbers.sort()

new_numbers = numbers[2:-2]

for n in new_numbers:
    print(n)

# # Exercise 6: Count the total number of digits in a number

n = int(input("Enter the integer: "))

print(len(str(n)))


# # Exercise 7: Print reverse number pattern

for b in range(5, 0, -1):  
    for i in range(b, 0, -1):
        print(i, end=" ")
    print()  
    

# # Exercise 8: Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]

rev_list1 = sorted(list1, reverse=True)

for num in rev_list1:
    print(num)

# # Exercise 9: Display numbers from -10 to -1 using a for loop

a = -10

while a <= -1:
    print(a)
    a+=1

# # Exercise 10: Display message “Done” after successful loop execution

a = 0 

while a<=4:
    print(a)
    a+=1
else:
    print('Done!')

# # Exercise 11: Print all prime numbers within a range

a = int(input('Enter the start point: '))
b = int(input('Enter the end point: '))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i ==0:
            return False
    return True

for n in range(a, b+1):
    if is_prime(n):
        print(n, end = ' ')

# # Exercise 12: Display Fibonacci series up to 10 terms

n = 10

a, b = 0, 1

for c in range(n):
    print(a, end = ' ')
    a, b = b, a+b

# # Exercise 13: Find the factorial of a given number

f = 1
n = int(input("Enter the integer: "))
for i in range(1, n+1):
    f *= i
print(f)

# # 14. Return Uncommon Elements of Lists

list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]

sum_list = list1 + list2
uncommon_elements = [n for n in sum_list if (n in list1 and n not in list2) or (n in list2 and n not in list1)]
print(uncommon_elements)
