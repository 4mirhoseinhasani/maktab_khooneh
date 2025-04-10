bazi = range(1,31)
emtiazat = 0
bord = 0
for emtiaz in bazi:
    emtiaz = int(input())
    emtiazat += emtiaz
    if emtiaz == 3:
        bord += 1
print(emtiazat, bord)