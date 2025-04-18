'''
In this exercise, you need to define a function called is_even that checks whether a given number is even or odd. This is a fundamental concept in mathematics and programming that is used in many problems.

Your Task:

Define a function called is_even(n) that:

Takes an integer n as input.
Checks if the number is even or not.
Returns the value True if the number is even.
Returns the value False if the number is odd.
The value must be returned, not printed directly.
Inputs:

An integer n that is read from the input.
Outputs:

The value True if the number is even.
The value False if the number is odd.
'''

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
number = int(input())
res = is_even(number)
print(res)