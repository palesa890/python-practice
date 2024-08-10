'''
Given the following buggy code, identify and correct the errors:

def sum_elements(lst):
    sum = 0
    for i in lst:
        summ += i
    return sum

numbers = [1, 2, 3, 4, 5]
result = sum_elements(numbers)
print(f"Sum of elements: {results}")

'''

def sum_elements(lst):
    summ = 0
    for i in lst:
        summ += i
    return summ

numbers = [1, 2, 3, 4, 5]
result = sum_elements(numbers)
print(f"Sum of elements: {result}")
