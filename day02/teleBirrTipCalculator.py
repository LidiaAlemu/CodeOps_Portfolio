def splitBill(total, people, tip_rate=0.10):
    """
    Calculate per person share including tip.
    
    Parameters:
        total (float): Bill amount in ETB
        people (int): Number of people splitting
        tipRate (float): Tip percentage as decimal (default 0.10)
    
    Returns:
        float: Amount each person pays
    """
    tipAmount = total * tip_rate
    totalWithTip = total + tipAmount
    perPerson = totalWithTip / people
    return perPerson



billTotal = 850.50  
numberOfPeople = 4  


perPersonShare = splitBill(billTotal, numberOfPeople)


friends = ["Almaz", "Dawit", "Tigist", "Hanna"]


print("TeleBirr Tip Calculator")
print("~" * 10)
print(f"Bill: {billTotal:.2f} ETB")
print(f"Tip: 10%")
print(f"People: {numberOfPeople}")
print(f"Each pays: {perPersonShare:.2f} ETB")

print("~" * 10)
for name in friends:
    print(f"{name}: {perPersonShare:.2f} ETB")
print("~" * 10)

print("Sent via TeleBirr")