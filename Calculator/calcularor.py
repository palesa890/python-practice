intro = "Hello! Welcome to Calculator.\nAsk me whatever you want to calculate!"
print(intro)

operator = input("These are the operators you can choose:\n1) Add\n2) Subtract\n3) Multiply\n4) Divide\nWhat would you like to do?: ")
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

if operator=='1':
    print(f'Your result is: {add(a,b)}')
elif operator=='2':
    print(f'Your result is: {subtract(a,b)}')
elif operator=='3':
    print(f'Your result is: {multiply(a,b)}')
elif operator=='4':
    print(f'Your result is: {divide(a,b)}')

