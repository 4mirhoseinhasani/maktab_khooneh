'''
In this exercise, you need to define a function called sum_numbers(*args) that can take any number of numbers and return their sum.

Your task:
Write a function called sum_numbers(*args) that: Takes an unlimited number of numbers as input.
Computes and returns the sum of these numbers.
If no numbers are passed, returns 0.

Inputs:
Zero or more integers that are passed to the sum_numbers function.

Outputs:
A number that represents the sum of all inputs.
If no inputs are passed, returns 0.
'''

def sum_numbers(*args):
    res = 0
    for number in args:
        res += number
    return res

input_list = list(map(int, input().split()))
# unpack list with *
print(sum_numbers(*input_list))