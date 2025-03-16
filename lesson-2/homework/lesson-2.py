# # # 1. Age Calculator
# # # Write a Python program to ask for a user's name and year of birth, then calculate and display their age.

from datetime import datetime
birth_date = int(input('Enter your date of birth: '))
name = input("Enter your name: ")
now = datetime.now().year
age = now - birth_date

print(f"{name} your age is {age}.")


# # # 2. Extract Car Names
# # # Extract car names from the following text:

txt1 = 'LMaasleitbtui'
print(txt1[::2])
print(txt1[1::2])


# # # 3. Extract Car Names
# # # Extract car names from the following text:

txt2 = 'MsaatmiazD'

print(txt2[::2])
print(txt2[-1:-11:-2])

# # # 4. Extract Residence Area
# # # Extract the residence area from the following text:

txt3 = "I'am John. I am from London"
print(txt3[21:29])

# # # 5. Reverse String
# # # Write a Python program that takes a user input string and prints it in reverse order.

txt4 = input('Enter your text: ')
print(txt4[::-1])

# # # 6. Count Vowels
# # # Write a Python program that counts the number of vowels in a given string.

vowels = ['a', 'e', 'i', 'o', 'u']  # list of vowels
string = list(input('Enter the text: '))   # given text
a = 0   # number of vowels
for letter in string:
    for letter1 in vowels:
        if letter == letter1:
            a+=1

print(f'In this text {a} vowel letters')

# # # 7. Find Maximum Value
# # # Write a Python program that takes a list of numbers as input and prints the maximum value.

numbers = []
n_of_numbers = int(input(f'How many numbers you want to enter: '))  # number of numbers
for n in range(n_of_numbers):
    numbers.append(int(input(f'Enter the {n+1} number: ')))     #adding numbers to the list

max_value = max(numbers)                                        # find maximum value
print(f'The maximum values among these numbers is {max_value}')


# # # 8. Check Palindrome
# # # Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

word = input(f'Enter word: ')
reversed_word = word[::-1]
if word.lower() == reversed_word.lower():
    print(f'This word is palindrome.')
else:
     print(f'This word is not palindrome.')


# # # 9. Extract Email Domain
# # # Write a Python program that extracts and prints the domain from an email address provided by the user.

email = input("Enter your email address: ").strip()

if "@" in email:
    domain = email.split("@")[1]
    print(f"Domain: {domain}")
else:
    print("Invalid email address")

# # # 10. Generate Random Password
# # # Write a Python program to generate a random password containing letters, digits, and special characters.
import random
import string

letters = string.ascii_letters
digits = string.digits
special_characters = string.punctuation
random_password = random.choice(letters) + random.choice(digits) + random.choice(special_characters)

print(random_password)
