#Temperature Label exercise

temperature = float(input("Enter the temperature in Celsius:"))

def temperature_label(temperature):
    if temperature < 15:
        return "cold"
    elif temperature < 28:
        return "warm"
    else:
        return "hot"

print(f"The temperature is {temperature_label(temperature)}.")

input("Press Enter to exit...")

print("~" * 15)


#Receit Loop Exercise

for i in range(1, 10):
    print(f"Receipt {i}:")

print("~" * 15)


#Even Numbers Exercise

number = 20
while number > 0:
    if number % 2 == 0:
        print(number)
    number -= 1

print("~" * 15)


#Discount Function Exercise

def apply_discount(price, percent=10):
    discount_amount = price * (percent / 100)
    final_price = price - discount_amount
    return final_price

# Example usage:
print(apply_discount(100, 20))

print("~" * 15)


#Countdown exercise
count = 5
while count > 0:
    print(f"{count} Liftoff!")
    count -= 1