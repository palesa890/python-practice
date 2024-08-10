'''
Create two sets:

    Set A: {1, 2, 3, 4, 5}
    Set B: {4, 5, 6, 7, 8}

Find the union, intersection, and difference between Set A and Set B.
Write a function is_subset(set_a, set_b) that checks if one set is a subset of another.
'''

setA = {1,2,3,4,5}
setB = {4,5,6,7,8}


union = setA | setB
print(f'union: {union}')

intersection = setA & setB
print(f'intersection: {intersection}')

diff = setA - setB
print(f'difference: {diff}')

def is_subset(set_a, set_b):
    if set_a.issubset(set_b):
        return "set_a is a subset of set_b"
    elif set_b.issubset(set_a):
        return "set_b is a subset of set_a"
    else:
        return "niether are subsets of eachother"
    
print(is_subset({5,4},setB))
