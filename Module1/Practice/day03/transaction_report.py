def main():
    total = {}
    
    try:
        with open("transaction.txt") as f:
            for line in f:
                line = line.strip() 
                if not line:
                    continue
                
                parts = line.split(",")
                name = parts[0].strip()
                amount = int(parts[1].strip())
                
                total[name] = total.get(name, 0) + amount
    except FileNotFoundError:
        print("No transaction file found")
        return
    
    customer = sorted(total.items(), key=lambda x: x[1], reverse=True)
    
    print("Customer Totals:")
    for name, total in customer:
        print(f"{name}: {total}ETB")
        
    with open("report.txt", "w") as f:
        f.write("Customer Totals\n")
        for name, total in customer:
            f.write(f"{name}: {total}ETB\n")
    print("Report saved to report.txt")
    
if __name__ == "__main__":
    main()