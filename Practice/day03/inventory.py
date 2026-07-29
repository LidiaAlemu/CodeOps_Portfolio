def load_stock(filename="stock.txt"):
    stock = {}
    
    try:
        with open(filename) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                item, qty = line.split(",")
                stock[item.strip()] = int(qty.strip())
        print(f"Loaded {len(stock)} items from {filename}")
        
    except FileNotFoundError:
        print(f"No existing stock file ('{filename}'). Starting empty.")
    return stock


def save_stock(stock, filename="stock.txt"):
    
    
    with open(filename, "w") as f:
        for item, qty in stock.items():
            f.write(f"{item},{qty}\n")
    print(f"Stock saved to {filename}")


def adjust(stock, item, amount):
    
    old_qty = stock.get(item, 0)
    stock[item] = old_qty + amount
    
    if stock[item] < 0:
        print(f"  Warning: {item} quantity would go negative. Setting to 0.")
        stock[item] = 0
    else:
        if amount > 0:
            print(f"  Restocked {amount} of {item}. New quantity: {stock[item]}")
        elif amount < 0:
            print(f"  Sold {abs(amount)} of {item}. New quantity: {stock[item]}")


def show_low_stock(stock, threshold=10):
   
    low_items = {item: qty for item, qty in stock.items() if qty < threshold}
    if low_items:
        print(f"\n Low stock (below {threshold}):")
        for item, qty in low_items.items():
            print(f"  - {item}: {qty} remaining")
    else:
        print(f"\nAll items have at least {threshold} units. Well stocked!")
    return low_items


def main():
    print("=== Pharmacy Inventory Tracker ===\n")


    stock = load_stock()

   
    print("\nCurrent Inventory:")
    for item, qty in stock.items():
        print(f"  {item}: {qty}")

    
    print("\n--- Processing today's adjustments ---")
    adjust(stock, "Paracetamol", -2)   
    adjust(stock, "Amoxicillin", -3)   
    adjust(stock, "CoughSyrup", -5)    
    adjust(stock, "VitaminC", 20)      
    adjust(stock, "Bandages", -10)    

    
    show_low_stock(stock)

    
    save_stock(stock)

    print("\nDone. Re-run the program to see the updated inventory.")

if __name__ == "__main__":
    main()