def bakhshseopanj(n):
    if n % 3 == 0 or n % 5 == 0:
        return True
    else:
        return False
    
sum = 0
for i in range(1,1000):
    if bakhshseopanj(i):
        sum = sum + i
        print(i,bakhshseopanj(i))
print(sum)