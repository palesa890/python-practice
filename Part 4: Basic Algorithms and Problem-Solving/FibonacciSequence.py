'''
Write a function fibonacci(n) that returns the first n numbers in the Fibonacci sequence.
'''

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))