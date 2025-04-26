"""
Write a decorator that calculates the execution time of a function and displays it after the function is executed. Then, use this decorator for a function that creates a list from 1 to n.

Input:
The number n that specifies the size of the list.

Output:
The function's return value (list 1 to n)
The execution time of the function in seconds
"""

import timeit
def run_time(function):
    def wrapper():
        timer = timeit.Timer(function).timeit(1)
        print(f"Time taken: {timer:.5f} seconds")
    return wrapper

@run_time
def make_list():
    list = []
    n = int(input("please enter a number: "))
    for n in range(1, n):
        list.append(n)
    return list

make_list()