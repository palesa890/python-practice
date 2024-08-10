'''
Create a list of integers from 1 to 10.
Write a function sum_list(lst) that returns the sum of all elements in the list.
Remove the last three elements from the list and print the modified list.
'''

lst = []
n = 10

for n in range(1,n+1):
    lst.append(n)

print(f'Here is a list of integers: {lst}')

def sum_list(lst):
    return sum(lst)

print(f'Here is the sum of all elements in the list: {sum_list(lst)}')

for i in range(3):
    lst.pop()
print(f'Here is the modified list: {lst}')