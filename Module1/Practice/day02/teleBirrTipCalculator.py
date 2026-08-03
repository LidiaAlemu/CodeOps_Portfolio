# In Class Exercise

def split_bill(total, people, tip_rate=0.10):
    """
    Calculate per person share including tip.
    
    Parameters:
        total (float): Bill amount in ETB
        people (int): Number of people splitting
        tip_rate (float): Tip percentage as decimal (default 0.10)
    
    Returns:
        float: Amount each person pays
    """
    tip_amount = total * tip_rate
    total_with_tip = total + tip_amount
    per_person = total_with_tip / people
    return per_person



bill_total = 850.50  
number_of_people = 4  


per_person_share = split_bill(bill_total, number_of_people)


friends = ["Almaz", "Dawit", "Tigist", "Hanna"]


print("TeleBirr Tip Calculator")
print("~" * 10)
print(f"Bill: {bill_total:.2f} ETB")
print(f"Tip: 10%")
print(f"People: {number_of_people}")
print(f"Each pays: {per_person_share:.2f} ETB")

print("~" * 10)
for name in friends:
    print(f"{name}: {per_person_share:.2f} ETB")
print("~" * 10)

print("Sent via TeleBirr")