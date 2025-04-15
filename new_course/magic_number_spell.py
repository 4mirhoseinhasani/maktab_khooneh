"""
In the land of wizards, there is an old spell that says that every magic number must have a special property:
If a number is divisible by 3, it is considered a magic number.
If a number is divisible by 5, it is considered a cursed number.
If a number is both magic and cursed, it is considered a legendary number.
Otherwise, it is a normal number.
Your task: Write a program that takes an integer as input and determines whether it is magic, cursed, legendary, or normal.
Make sure that the words in the quotes are displayed exactly as the output.
Input:
An integer n
Output:
If n is divisible by 3, print: "جادویی"
If n is divisible by 5, print: "نفرین شده"
If n is divisible by both, print: "افسانه ای"
Otherwise, print: "معمولی"
"""
n = int(input())
if n % 3 == 0 and n % 5 == 0:
    print("افسانه ای")

elif n % 5 == 0:
    print("نفرین شده")

elif n % 3 == 0:
    print("جادویی")
else:
    print("معمولی")
