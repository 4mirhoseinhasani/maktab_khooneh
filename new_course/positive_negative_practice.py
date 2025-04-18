'''
My task:
Write a function called is_positive that takes a number and returns True if it is positive or zero, and False otherwise.

Inputs:
An integer (int).

Outputs:
A True value if it is positive or zero.
A False value if it is negative.
'''

def is_positive(number):
    if number >= 0:
        return True
    else:
        return False

number = int(input())
res = is_positive(number)
print(res)