'''
Create a Python module called math_operations.py with the following functions:

    add(a, b): Returns the sum of two numbers.
    subtract(a, b): Returns the difference between two numbers.
    multiply(a, b): Returns the product of two numbers.
    divide(a, b): Returns the quotient of two numbers (handle division by zero).

Import the module in another Python file and use all the functions in math_operations.py.
'''
from math_operations import add, subtract, multiply, divide  

a = int(input("add first number: "))
b = int(input("add second number: "))
operation = input("choose between +, -, * and / as an operation: ")

def calculator(a,b,operation):
    if operation == "+":
        return add(a,b)
    elif operation == "-":
        return subtract(a,b)
    elif operation == "*":
        return multiply(a,b)
    elif operation == "/":
        return divide(a,b)
    else:
        return "wrong operation, try again"
    
print(calculator(a,b,operation))

operations = ['+','-','*','/']
while operation in operations:
    calculator(a,b,operation)

