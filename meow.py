# print("Hello world!")


# Strings
name = "Alex"
# Integer (Whole numbers)
age = 25
# Float (decimal number)
height = 9.5
# Boolean
is_student = True

# print("Hey my name is " + name)
# print("Hey my name is", name)

# print(name[-1])

# Python is a case-sensitive language, so "Hello" and "hello" are different words.

message = "hello world"
print(message.upper())
print(message.lower())
print(message.capitalize())
print(message.replace("l", "L"))
print("World" in message)
print(len(message))

greeting1 = "Hello"
greeting2 = "hello"

if greeting1 == greeting2:
    print("They are the same")
else:
    print("They are different")

# Type conversion
age_str = "30"
age_num = int(age_str)
print(type(age_num))
print(type(age_str))

price_float = 29.99
price_int = int(price_float)


import math
# basic operations
x = 10
y = 5

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x % y)
print(x**y)

# x = x + 15
x += 15
print(x)

# string concatination
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

print("Hey my name is " + first_name + " and my last name is " + last_name)

# f strings
print(f"Hey my name is {first_name} and my last name is {last_name}")

# int floor division
a = 17
b = 5
print(a / b)  # result 3 (rounds down) normally it is 3.4
print(a // b)  # result 3 (rounds down) normally it is 3.4

# assing multiple values
i, j, k = 1, 2, 3
print(i, j, k)

# swap values
m = 10
n = 20
m, n = n, m
print(m, n)

# comparions operators
c = 5
d = 10

print(c == d)
print(c != d)
print(c > d)
print(c < d)
print(c >= d)
print(c <= d)

# logical operators
a = True
b = False


print(a and b)
print(a or b)
print(not b)


# string slicing
text = "Python programming"
print(text[0:7])
print(text[7:])
print(text[::-1])

# String formatting with .format()
name = "Alice"
age = 25
msg = "My name is {} and I am {} years old".format(name, age)
print(msg)

# Using placeholders
msg2 = "My name is {0} and I am {1} years. {0} is a nice name".format(
    name, age)
print(msg2)

# math module operations
print(math.pi)
print(math.sqrt(16))
print(math.floor(4.7))  # 4.0
print(math.ceil(5.3))  # 6.0
print(math.pow(2, 3))  # 8

pi = 3.141592653589793
print(round(pi, 2))


# name = input("What is your name? ")
# print("Hello", name)

# age = int(input("How old are you? "))
# years_to_100 = 100 - age
# print(f"You will be 100 in {years_to_100} years")

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# sum_result = num1 + num2
# print(f"The sum of {num1} and {num2} is {sum_result}")


# Working with multiple inputs on one line
# x, y = input("Enter two values seperated by space: ").split()
# print(f"first value: {x}, second value: {y}")


user_choice = input("Choose a color (or press Enter for default): ")
if user_choice == "":
    user_choice = "blue"

print(f"Selected color: {user_choice}")


# possiblities are endless
length = float(input("Enter length in meters: "))
print(f"That's {length * 100} centimeters")


# Python uses indentation to define blocks of code, not curly brackets or other symbols.

temp = 28
if temp > 30:
    print("It's hot outside")
elif temp > 20:
    print("It's a nice day!")
else:
    print("It's cold outside")


# Checking multiple conditions with logical operators
age = 25
has_licence = True

if age >= 18 and has_licence:
    print("you can drive a car")
elif age >= 18 and not has_licence:
    print("you need to get a driver's lincese first")
else:
    print("You are too young to drive.")


# Nested conditionals
score = 85

if score >= 60:
    print("You passed!")
    if score >= 90:
        print("You got an A")
    elif score >= 80:
        print("You got a B!")
    elif score >= 70:
        print("You got a C!")
    else:
        print("You got a D!")
else:
    print("You failed")


# using the "in" operator with conditionals
fruit = "apple"
if fruit in ["banana", "orange"]:
    print(f"{fruit} is in the list")


# Ternary operator (one-line if-else)
age = 20
status = "adult" if age >= 18 else "minor"
print(f"Status: {status}")


# Comparing strings
password = "secret123"
if password == "secret123":
    print("Access granted")
else:
    print("No access!")

# Chaining comparisons
x = 15
if 10 < x < 20:
    print("x is between 10 and 20")


# truthy or falsy
user_input = ""
if user_input:
    print("Input provided.")
else:
    print("no input provided")


# For loop
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

print("\nReversed counting from 5 to 1:")
for i in range(5, 0, -1):
    print(i)

# While loop
count = 1
print("While loop")
while count <= 5:
    print(count)
    count += 1

# Reversed while loop
count = 5
print("\nReversed While loop")
while count >= 1:
    print(count)
    count -= 1


# Looping thru a list
fruits = ["apple", "banana", "cherry"]
print("My fruits:")
for fruit in fruits:
    print(fruit)

# Reversing a list
print("\nMy fruits in reverse:")
for fruit in reversed(fruits):
    print(fruit)


# Loop with enumerate
print("fruit with indicies:")
for index, fruit in enumerate(fruits):
    print(f"{index}:{fruit}")


# loop with Dictionaries
person = {"name": "John", "age": 30, "city": "NYC"}
print("\nPerson dict")
for key, value in person.items():
    print(f"{key}:{value}")

# List comprehension (compact loop for creating lists)
squares = [x**2 for x in range(1, 6)]
print("Squares from 1 to 5", squares)


# For loop wit zip() - iterate through multiple lists in parallel
colors = ["red", "yellow", "green"]

print("\nFruits and their colors:")
for fruit, color in zip(fruits, colors):
    print(f"{fruit} is {color}")


# Break and continue
print("\n Loop with break")
for i in range(1, 10):
    if i > 5:
        break
    print(i)

print("\n Loop with continue")
for i in range(1, 10):
    if i % 2 == 0:
        continue  # skip even numbers
    print(i)


# Infinite loops with break condition
print("\nControlled infinite loop:")
i = 1
while True:
    print(i)
    i += 1
    if i > 5:
        break



# Functions are blocks of code that can be reused, they can take arguments and return values

# def greet_everyone():
#     print("Hello everyone!")


# greet_everyone()


# def greet(name):
#     print("Hello,", name)


# greet("John")
# greet("Jane")
# greet("Kyle")

# An example: without functions
# user1 = "Emma"
# print("Hello,", user1, "Welcome to our app")
# print("We hope you enjoy using our services.")
# print("Let us know if you need any help.")

# user2 = "John"
# print("Hello,", user2, "Welcome to our app")
# print("We hope you enjoy using our services.")
# print("Let us know if you need any help.")

# user3 = "Bob"
# print("Hello,", user3, "Welcome to our app")
# print("We hope you enjoy using our services.")
# print("Let us know if you need any help.")


# With functions
def greet_user(name):
    print("Hello,", name, "Welcome to our app")
    print("We hope you enjoy using our services.")
    print("Let us know if you need any help.")


greet_user("Emma")
greet_user("John")
greet_user("Bob")


def power(base, exponent):
    return base ** exponent


# x = power(2, 5)  # 32
# y = power(8, 2)  # 64
# z = power(3, 3)  # 27

print(power(2, 5))
print(power(8, 2))
print(power(3, 3))



# Lists are collections of items that can store different types of data

numbers = [1, 2, 3, 4, 5]
print(numbers[0])
numbers[1] = 22
numbers.append(55)
numbers.remove(3)

print(numbers)
print(len(numbers))

# Slicing lists
numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])  # Elements from index 1 to 3
print(numbers[::2])  # Every other element
print(numbers[::-1])  # Reverse the list
print(numbers + [6, 7, 8])  # Concatenate lists
print(numbers * 2)  # Repeat the list


# Dictionaries are collections that store data as key-value pairs.
student = {
    "name": "Emma",
    "age": 22,
    "courses": ["Math", "Computer Science"]
}

print(student["name"])
student["grade"] = "A"
student["age"] += 10
print(student)
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(f"{key}: {value}")


# Sets are unordered collections of unique items. - No duplicates allowed
unique_colors = {"red", "blue", "green", "green"}
print("unique colors:", unique_colors)

# Tuples are ordered collections that cannot be changed after creation.
coordinates = (10.5, 20.8)


try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"10 divided by {number} is {result}")
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You cannot divide by zero!")
finally:
    print("This piece of code will always run!")


import random
import math
import datetime
import os
import sys
import time

# Get a random number
random_number = random.randint(1, 10)  # 1 and 10 is included
print(f"Random number is {random_number}")

# choose a random element from a list
fruits = ["apple", "orange", "cherry", "banana"]
random_fruit = random.choice(fruits)
print(f"Random fruit is {random_fruit}")

# shuffle the list
random.shuffle(fruits)
print(f"Shuffled list: {fruits}")

# Math module
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Pi: {math.pi}")
print(f"Ceiling of 4.3: {math.ceil(4.3)}")
print(f"Floor of 4.8: {math.floor(4.8)}")
print(f"5 raised to power 3: {math.pow(5, 3)}")


# Datetime module
current_time = datetime.datetime.now()
print(f"Current date and time: {current_time}")
print(f"Today's date: {datetime.date.today()}")
print(f"Current year: {datetime.date.today().year}")

# OS module
current_directory = os.getcwd()
print(f"Current directory: {current_directory}")
print(f"List of files: {os.listdir('.')}")


# Time module
print("Waiting for 2 seconds...")
time.sleep(2)
print("Done!")

# Sys module
print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")  # e.g., 'win32', 'darwin', 'linux'
