"""
We have a machine called the “magic machine” that takes a prime number n and wants to get to 1. The machine can do two things:
If the current number is divisible by 2, it halve it.
If the current number is not divisible by 2, it multiplies the number by 3 and adds 1 to it.
Your task is to write a program that takes the prime number n as input and show how the machine gets to 1.
Input:
An integer n (2 ≤ n ≤ 1000)
Output:
At each step, print the current value of n until the number reaches 1.
"""
n = int(input())
print(n)
while n > 1:
    if n % 2 == 0:
        n = n / 2
        print(int(n))
    elif n % 2 != 0:
        n = (n * 3) + 1
        print(int(n))
    elif n == 1:
        print(1)