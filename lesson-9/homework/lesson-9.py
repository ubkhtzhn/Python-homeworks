# # 1. Circle Class
# # Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
import math

class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        s = math.pi * self.r**2
        return s

    def perimeter(self):
        l = 2*math.pi*self.r
        return l

# # 2. Person Class
# # Write a Python program to create a Person class. Include attributes like name, country, and date of birth.
# # Implement a method to determine the person's age.

from datetime import datetime

current_year = datetime.now().year

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
    
    def age(self):
        a = current_year - int(self.date_of_birth)
        return a
    
n = Person('Baxitjan', 'Uzbekistan', 2002)

print(n.age())


# # 3. Calculator Class
# # Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.

class Calculator:
    def __init__(self):
        pass

    def subtraction(self):
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        return a - b

    def sum(self):
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        return a + b

    def multiplication(self):
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        return a * b

    def division(self):
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b



while True:
    calc = Calculator()

    print("0. Stop")
    print("1. Sum")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Choose an operation (1-4): ")

    if choice == "1":
        print("Result:", calc.sum())
    elif choice == "2":
        print("Result:", calc.subtraction())
    elif choice == "3":
        print("Result:", calc.multiplication())
    elif choice == "4":
        print("Result:", calc.division() )
    elif choice == "0":
        break
    else:
        print("Invalid choice!")

# # 4. Shape and Subclasses
# # Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. 
# # Implement subclasses for different shapes like Circle, Triangle, and Square.

import math

class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius**2
    def perimeter(self):
        return 2*math.pi*self.radius
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        p = (self.a+self.b+self.c)/2
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**(1/2)
    def perimeter(self):
        return self.a + self.b + self.c
    
class Square(Shape):
    def __init__(self, a):
        self.a = a
    def square(self):
        return self.a**2
    def perimeter(self):
        return 4* self.a


shapes = [Circle(3), Triangle(3, 4, 5), Square(4)]

for shape in shapes:
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())


# # 5. Binary Search Tree Class
# # Write a Python program to create a class representing a binary search tree. 
# # Include methods for inserting and searching for elements in the binary tree.

class Node:
    def __init__(self, value):
        self.value = value  # Значение узла
        self.left = None    # Левый потомок
        self.right = None   # Правый потомок


class BinarySearchTree:
    def __init__(self):
        self.root = None  # Корень дерева

    def insert(self, value):
        # Если дерево пустое, создаём корень
        if self.root is None:
            self.root = Node(value)
        else:
            # Если не пустое, добавляем в правильную позицию
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        # Если значение меньше текущего узла, идём влево
        if value < node.value:
            if node.left is None:
                node.left = Node(value)  # Вставляем новый узел
            else:
                self._insert_recursive(node.left, value)  # Рекурсивно идём дальше влево
        # Если значение больше текущего узла, идём вправо
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)  # Вставляем новый узел
            else:
                self._insert_recursive(node.right, value)  # Рекурсивно идём дальше вправо

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        # Если узел пустой, значит, не нашли
        if node is None:
            return False
        # Если нашли совпадение
        if node.value == value:
            return True
        # Если значение меньше, идём влево
        elif value < node.value:
            return self._search_recursive(node.left, value)
        # Если больше, идём вправо
        else:
            return self._search_recursive(node.right, value)

# Создаём дерево
bst = BinarySearchTree()

# Вставляем элементы
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(18)

# Ищем элементы
print(bst.search(7))  # True, так как 7 есть в дереве
print(bst.search(9))  # False, так как 9 нет в дереве


# # 6. Stack Data Structure
# # Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.


class Stack:
    def __init__(self):
        self.stack = []  # Инициализация пустого стека

    def push(self, item):
        """Добавить элемент в стек."""
        self.stack.append(item)

    def pop(self):
        """Удалить и вернуть верхний элемент стека."""
        if not self.is_empty():  # Проверяем, что стек не пуст
            return self.stack.pop()
        else:
            return "Stack is empty!"  # Если стек пуст, вернуть сообщение

    def peek(self):
        """Посмотреть верхний элемент стека без его удаления."""
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty!"

    def is_empty(self):
        """Проверить, пуст ли стек."""
        return len(self.stack) == 0

    def size(self):
        """Вернуть количество элементов в стеке."""
        return len(self.stack)


# # 8. Shopping Cart Class
# # Write a Python program to create a class representing a shopping cart. 
# # Include methods for adding and removing items, and calculating the total price.

class ShoppingCart:
    def __init__(self):
        self.products = []
    
    def add_product(self, name, price):
        product = {'name': name, 'price': price}
        self.products.append(product)

    def remove(self, name):
        for p in self.products:
            if p['name'] == name:
                self.products.remove(p)
                return f"{p} is removed"
        return f"{name} not found in the products"
    
    def total(self):
        s = sum(product['price'] for product in self.products)
        return s
    
    def all_products(self):
        if not self.products:
            return f'Your products is empty'
        return [p['name'] for p in self.products]

            
cart = ShoppingCart()

cart.add_product('Apple', 12000)
cart.add_product('Banana', 22000)
cart.add_product('Orange', 16000)

print(cart.all_products())
print(cart.total())
print(cart.remove('Banana'))

print(cart.all_products())
print(cart.total())


# # 9. Stack with Display
# # Write a Python program to create a class representing a stack data structure. 
# # Include methods for pushing, popping, and displaying elements.


class Stack:
    def __init__(self):
        self.stack = [] 

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():  
            return self.stack.pop()
        else:
            return "Stack is empty!"  

    def display(self):
        if not self.is_empty():
            return self.stack
        else:
            return "Stack is empty!"

    def is_empty(self):
        return len(self.stack) == 0
