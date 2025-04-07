# # 1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

try:
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))

    result = a/b
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")
else:
    print('Результат: ', result)


# # 2. Write a Python program that prompts the user to input an integer and raises a ValueError 
# # exception if the input is not a valid integer.

while True:
    try:
        chislo  = int(input('Введите целое число: '))
        break
    except ValueError:
            print('Введите только целое число!')


# # 3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

file = "data.txt"

try:
    with open(file) as f:
        text = f.read()
except FileNotFoundError:
    pass


# # 4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception 
# # if the inputs are not numerical.

while True:
    try:
        a1 = float(input('Введите первое число: '))
        a2 = float(input('Введите второе число: '))
        break
    except TypeError:
        print('Введите только числовое значение! ')
    except ValueError:
        print('Введите только числовое значение!')

# # 5. Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.

try:
    with open('text.txt', 'w') as f:
        f.write('Hello')
except PermissionError:
    pass


# # 6. Write a Python program that executes an operation on a list and handles an 
# # IndexError exception if the index is out of range.

my_list = [1, 2, 3, 4]

try:
    print(my_list[5])
except IndexError:
    pass

# # 7. Write a Python program that prompts the user to input a number and 
# # handles a KeyboardInterrupt exception if the user cancels the input.

try: 
    b = input()
except KeyboardInterrupt:
    pass

# # 8. Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.

x = 5
y = 0

try:
    print(x/y)
except ArithmeticError:
    pass

# # 9. Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.

try:
    with open('text.txt') as file1:
        file1.read()
except UnicodeDecodeError:
    print('Unicode Error!')

# # 10. Write a Python program that executes a list operation and handles 
# # an AttributeError exception if the attribute does not exist.

try:
    text = 'list'
    text.append(1)
except AttributeError:
    pass 


###############################################################################################################

# # 1. Write a Python program to read an entire text file.

with open('text.txt') as file:
    print(file.read())

# # 2. Write a Python program to read first n lines of a file.

n = int(input("Enter number of lines: "))

with open('text.txt') as file:
    for l in range(n):
        line = file.readline()
        print(line.strip())

# # 3. Write a Python program to append text to a file and display the text.

with open('text.txt', 'a') as file:
    file.write('World')

with open('text.txt') as file2:
    b = file2.read()
    print(b)

# # 4. Write a Python program to read last n lines of a file.

n = int(input("Enter number of lines: "))

with open('text.txt') as file:
    lines3 = file.readlines()

for lin in lines3[-n:]:
    print(lin.strip())

# # 5. Write a Python program to read a file line by line and store it into a list.

with open('text.txt') as file:
    lines2 = file.readlines()
    list1 = []
for line in lines2:
    print(line.strip())
    list1.append(line.strip())
print(list1)

# # # 6. Write a Python program to read a file line by line and store it into a variable.

with open('text.txt') as file:
    lines1 = file.readlines()
for l in lines1:
    print(l.strip())
print(lines1)

# # 7. Write a Python program to read a file line by line and store it into an array.

with open('text.txt') as file:
    lines4 = file.readlines()
    my_list = []
for l in lines4:
    print(l.strip())
    my_list.append(l.strip())
print(my_list)

# # 8. Write a Python program to find the longest words.

with open('text.txt') as file:
    words = file.read().split()
max_len = max(len(word) for word in words)

longest_word = [word for word in words if len(word) == max_len]

for w in longest_word:
    print(w)

# # 9. Write a Python program to count the number of lines in a text file.

with open('text.txt') as file:
    n = len(file.readlines())
print(n)

# # 10. Write a Python program to count the frequency of words in a file.

from collections import Counter

with open('text.txt', encoding='utf-8') as file:
    text = file.read()

words = text.split()

word_counts = Counter(words)

print("Частота слов в файле:")
for word, count in word_counts.items():
    print(f"{word}: {count}")

# # 11. Write a Python program to get the file size of a plain file.

import os

file_path = 'text.txt'

file_size = os.path.getsize(file_path)

print(f"Размер файла '{file_path}': {file_size} байт")

# # # 12. Write a Python program to write a list to a file.

with open('text.txt', 'w') as file:
    liist = [1, 2, 3]
    a = file.write(str(liist))

with open('text.txt') as f:
    r = f.read()

print(r)

# # 13. Write a Python program to copy the contents of a file to another file.

with open('text2.txt') as file:
    context = file.read()

with open('text.txt', 'w') as file2:
    content = file2.write(context)

# # 14. Write a Python program to combine each line from the first file with the corresponding line in the second file.

with open('text.txt') as file1:
    f1 = file1.readlines()  

with open('text2.txt') as file2:
    f2 = file2.readlines()  

for line1, line2 in zip(f1, f2):
    print(line1.strip() + ' ' + line2.strip()) 

# # 15. Write a Python program to read a random line from a file.

import random

with open('text.txt', 'r') as file:
    lines = file.readlines()

random_line = random.choice(lines)

print(random_line.strip())

# # 16. Write a Python program to assess if a file is closed or not.

file = open('text.txt')

if file.closed:
    print('File is closed')
else:
    print('File is not closed')

# # 17. Write a Python program to remove newline characters from a file.

with open('text.txt') as file:
    content = file.read().replace('\n', '')

print(content)

# # 18. Write a Python program that takes a text file as input and returns the number of words in a given text file.

import re

with open('text.txt', 'r') as file:
    content = file.read()

words = re.findall(r'\b\w+\b', content)

print("Number of words:", len(words))

# # 19. Write a Python program to extract characters from various text files and put them into a list.

import os

filenames = ['file1.txt', 'file2.txt', 'file3.txt']

char_list = []

for filename in filenames:
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read()
            char_list.extend(list(content)) 

print(char_list)

# # 20. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.

import string

for letter in string.ascii_uppercase:
    filename = f"{letter}.txt"
    with open(filename, 'w') as file:
        file.write(f"This is file {filename}\n") 

# # 21. Write a Python program to create a file where all 
# # letters of the English alphabet are listed with a specified number of letters on each line.

import string

letters_per_line = 5  

alphabet = string.ascii_lowercase

with open('alphabet.txt', 'w') as file:
    for i in range(0, len(alphabet), letters_per_line):
        line = alphabet[i:i+letters_per_line]
        file.write(line + '\n')
