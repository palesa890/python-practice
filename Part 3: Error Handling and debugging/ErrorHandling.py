'''
Write a function divide_numbers(a, b) that divides two numbers and handles the case where b is zero by returning an appropriate error message.
Implement a try-except block to handle any errors that might occur during the input of two integers by a user.
'''

def divide_numbers(a,b):
    try:
        return a/b
    except ZeroDivisionError :
        return "you cannot divide by zero"
try:
    a = int(input("Enter the first integer: "))
    b = int(input("Enter the second integer: "))
    print(divide_numbers(a, b))
except ValueError:
    print("Error: Please enter valid integers.")

# print(divide_numbers(a,b))