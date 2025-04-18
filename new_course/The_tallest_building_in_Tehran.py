'''
Tallest Building on the Skyline
You need to write a function called skyline(*args) that takes the height of a number of buildings and returns the tallest.

Your task:
Write a function called skyline(*args) that: Takes a number of integers (the heights of the buildings) as input.
Finds and returns the largest of them.
If no numbers are entered, returns 0.

Inputs:
A number of integers representing the heights of the buildings.

Outputs:
An integer that identifies the tallest building.
If no values ​​are given, returns 0.
'''

def skyline(*args):
    tallest = 0
    for building in args:
        if building >= tallest:
            tallest = building
    return tallest

input_list = list(map(int, input().split()))
res = skyline(*input_list)
print(res)
