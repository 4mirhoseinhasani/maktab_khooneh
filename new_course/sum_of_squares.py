'''
My task:
In this exercise, you need to write a function that takes two integers and calculates the sum of their squares.

Your task:
Write a function called sum_of_squares that takes two integers and returns the sum of the squares of those two numbers.

Calculation formula:

sum_of_squares(a,b)=a**2+b**2
'''

def sum_of_squares(a, b):
    return a**2 + b**2

a = int(input())
b = int(input())
res = sum_of_squares(a, b)
print(res)