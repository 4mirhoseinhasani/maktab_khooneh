'''
In this exercise, you need to define a function called is_greater(a, b) that checks whether the number a is greater than b.

Your Task:

Define a function called is_greater(a, b) that:

Takes two integers a and b as input.
Checks if a is greater than b.
Returns the value True if a > b.
Returns the value False if a ≤ b.
The value must be returned, not printed directly.
Inputs:

Two integers a and b that are read from the input.
Outputs:

The value True if a is greater than b.
The value False if a is less than or equal to b.
'''

def is_greater(a, b):
    if a > b:
        return True
    elif a <= b:
        return False

a = int(input())
b = int(input())
res = is_greater(a, b)
print(res)