n = float(input('please give me a number : '))

items = 0
total = 0

while n != -1:
    total += n
    items += 1
    miangin = total/items
    print(miangin)
    n = float(input('please give me a number : '))

print('miangin ma = ', miangin)