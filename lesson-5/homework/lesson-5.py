# # # 1. def is_leap(year): """ Determines whether a given year is a leap year.

def is_leap(year):
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    if (year%4==0 and year%100!=0) or year%400==0:
        return "This is leap year"
    else:
        return "This is not leap year"


# # # 2. Conditional Statements Exercise

# # # Given an integer, n, perform the following conditional actions:

# # # If n is odd, print Weird
# # # If n is even and in the inclusive range of 2 to 5, print Not Weird
# # # If n is even and in the inclusive range of 6 to 20, print Weird
# # # If n is even and greater than 20, print Not Weird

n = int(input("Enter integer: "))

if n%2==1:
    print("weird")
elif 2 <= n <= 5:
    print('not weird')
elif 6 <= n <= 20:
    print("weird")
else:
    print('not weird')
    

# # # 3. Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.
# # # Give two solutions.

# # # Solution 1 with if-else statement.

# # # Solution 2 without if-else statement.

a = int(input('Enter the first integer: '))
b = int(input('Enter the second integer: '))
c = []

if a<b:
    if a%2 != 0:
        a +=1
    while a<=b:
        c.append(a)
        a += 2
else:
    print("The first integer must be less than the second integer.")

print(c)

def even_numbers(a, b):
    a+=a%2
    b-=b%2

    return list(range(a, b+1, 2))*(a<=b)


print(even_numbers(2,8))
