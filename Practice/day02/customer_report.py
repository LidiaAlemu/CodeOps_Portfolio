customers = [
    ("Lidia", 2000), ("Meskerem", 3000), ("Rebka", 500), ("Melese", 300), ("Amanuel", 700), ("Yonas", 2250)
]

def tier(balance):
    if balance >= 1000:
        return "Premium"
    elif balance >= 500:
        return "Standard"
    else:
        return "Basic"
    

for name, balance in customers:
    print(f"Customer: {name}, Balance: ${balance}, Tier: {tier(balance)}")