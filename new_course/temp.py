donationds = {
    'amirhosein': 1750,
    'reza': 5586,
    'nahid': 4738,
    'hamidreza': 5586,
    'atefeh': 8585,
    'rozita': 90
    }

def donate_analityze(donates):
    best_donate = -1
    best_donator = ""
    total_donates = 0
    count = 0
    for name , donate_price in donates.items():
        total_donates += donate_price
        count += 1 
        
        if donate_price > best_donate or (donate_price == best_donate and name > best_donator):
            best_donator = name
            best_donate = donate_price
    
    avg_donates = total_donates / count

    return best_donate , best_donator , avg_donates , total_donates


best_donate , best_donator , avg_donates , total_donates = donate_analityze(donationds)

print(f"my best donator is {best_donator} with {int(best_donate)} $")
print(f"total donations is {int(total_donates)} $", end=" ||| ")
print(f"avarage of donates is {avg_donates:.2f} $ . thanks All :)")

