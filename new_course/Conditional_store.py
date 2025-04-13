purchase_amount = int(input())
if purchase_amount > 50000:
    purchase_amount = purchase_amount * 0.8
    print(int(purchase_amount))
elif 2000 < purchase_amount < 50000:
    purchase_amount = purchase_amount * 0.9
    print(int(purchase_amount))
elif purchase_amount < 20000:
    print(int(purchase_amount))