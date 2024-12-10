def gcd(x, y):
    # etminan az inke x > y ke agar nabood , jashoon ro avaz kon!
    if x < y:
        x, y = y, x

    for _ in range(y, 0, -1):
        if y == 0:  # agar y == 0 shod , break bede!
            break
        baghimande = x % y
        x = y
        y = baghimande

    return x

print("GCD 12 & 18 = " , gcd(12, 18))