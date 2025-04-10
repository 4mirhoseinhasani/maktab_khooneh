def divide(n):
    divisor_count = 1
    for divisor in range(1, n):
        if n % divisor == 0:
            divisor_count +=1
    return divisor_count

numbers = []
for _ in range(20):
    num = int(input())
    numbers.append(num)

max_divisor = 0
result_number = 0
for num in numbers:
    divisor = divide(num)
    if divisor > max_divisor or (divisor == max_divisor and num > result_number):
        max_divisor = divisor
        result_number = num

print(result_number, max_divisor)