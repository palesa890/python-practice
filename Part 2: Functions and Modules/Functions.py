'''
Write a function factorial(n) that computes the factorial of a non-negative integer n.
Create a function find_max(lst) that returns the maximum value from a list of numbers.
Write a function reverse_string(s) that takes a string and returns it in reverse order.
'''
import math

def factorial(n):
    return math.factorial(n)

print(factorial(10))

lst = [1,2,3,4,5]
def find_max(lst):
    return max(lst)

print(find_max(lst))

def reverse_string(s):
    return s[::-1]

print(reverse_string("palesa"))