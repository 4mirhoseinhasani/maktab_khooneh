"""
My task:
A wizard has decided to increase the power of numbers using a special spell! He chooses a number n and then, for n steps, does the following:
If the number is odd, doubles its value and subtracts 1 unit.
If the number is even, halve its value.
The wizard performs this operation exactly n times.
📝 Input:
An integer n that specifies the number of steps (1 ≤ n ≤ 20).
An integer x that is the initial value (1 ≤ x ≤ 1000).
📤 Output:
Finally, display the final value of x.
"""
n = int(input())
x = int(input())

for _ in range(n):
    if x % 2 == 0:
        x = x/2
    else:
        x = (x * 2) - 1
print(int(x))