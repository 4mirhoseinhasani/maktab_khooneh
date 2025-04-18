'''
In this exercise, you need to write a function called pick_evens(*args) that takes a series of numbers and returns only even numbers.

Your task:
Write a function called pick_evens(*args) that: Takes an unlimited number of numbers as input.
Returns only even numbers as a list.
If there are no even numbers, return an empty list [].

Inputs:
Multiple integers that are passed to the pick_evens function.

Outputs:
A list containing only even numbers.
If there are no even numbers in the input, return an empty list [].
'''

def pick_evens(*args):
    evens = []
    for n in args:
        if n % 2 == 0:
            evens.append(n)
    return evens

input_list = list(map(int, input().split()))
res = pick_evens(*input_list)
print(res)