# Advanced Calculator
import math
import random

first_string = input("Enter a number: ") # 1
second_string = input("Enter the second number: ") # 2

operation_selection = input("Enter the operation: ") # +

# add function
def add(input_first_string, input_second_string):
    return float(input_first_string) + float(input_second_string)

# subtract function
def subtract(input_first_string, input_second_string):
    return float(input_first_string) - float(input_second_string)

# multiply function
def multiply(input_first_string, input_second_string):
    return float(input_first_string) * float(input_second_string)

# divide function
def divide(input_first_string, input_second_string):
    return float(input_first_string) / float(input_second_string)

# Modulus function
def modulus(input_first_string, input_second_string):
    return float(input_first_string) % float(input_second_string)

# Exponent function
def exponent(input_first_string, input_second_string):
    return float(input_first_string) ** float(input_second_string)

# Floor division function
def floor_division(input_first_string, input_second_string):
    return float(input_first_string) // float(input_second_string)

# Square root function
def square_root(input_first_string):
    return float(input_first_string) ** 0.5

# Cube root function
def cube_root(input_first_string):
    return float(input_first_string) ** (1/3)

# Logarithm function
def logarithm(input_first_string):
    return math.log(float(input_first_string))

# Sine function
def sine(input_first_string):
    return math.sin(float(input_first_string))

# Cosine function
def cosine(input_first_string):
    return math.cos(float(input_first_string))

# Tangent function
def tangent(input_first_string):
    return math.tan(float(input_first_string))

# Factorial function
def factorial(input_first_string):
    return math.factorial(int(input_first_string))

# Power function
def power(input_first_string, input_second_string):
    return float(input_first_string) ** float(input_second_string)

# Absolute value function
def absolute_value(input_first_string):
    return abs(float(input_first_string))

# Random number function
def random_number():
    return random.random()


# Operation selection
if operation_selection == "+":
    print('The result is: ', add(first_string, second_string))
elif operation_selection == "-":
    print('The result is: ', subtract(first_string, second_string))
elif operation_selection == "*":
    print('The result is: ', multiply(first_string, second_string))
elif operation_selection == "/":
    print('The result is: ', divide(first_string, second_string))
elif operation_selection == "%":
    print('The result is: ', modulus(first_string, second_string))
elif operation_selection == "**":
    print('The result is: ', exponent(first_string, second_string))
elif operation_selection == "//":
    print('The result is: ', floor_division(first_string, second_string))
elif operation_selection == "sqrt":
    print('The result is: ', square_root(first_string))
elif operation_selection == "cbrt":
    print('The result is: ', cube_root(first_string))
elif operation_selection == "log":
    print('The result is: ', logarithm(first_string))
elif operation_selection == "sin":
    print('The result is: ', sine(first_string))
elif operation_selection == "cos":
    print('The result is: ', cosine(first_string))
elif operation_selection == "tan":
    print('The result is: ', tangent(first_string))
elif operation_selection == "fact":
    print('The result is: ', factorial(first_string))
elif operation_selection == "pow":
    print('The result is: ', power(first_string, second_string))
elif operation_selection == "abs":
    print('The result is: ', absolute_value(first_string))
elif operation_selection == "random":
    print('The result is: ', random_number())
else:
    print("Invalid operation")
