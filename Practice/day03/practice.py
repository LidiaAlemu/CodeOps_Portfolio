# Unique Cities

print("1. Unique cities")
cities = ['Addis Ababa', 'Adama', 'Hawassa', 'Dire Dawa', 'New York', 'Adama', 'Addis Ababa']

unique_cities = set(cities)
print("Cities:", unique_cities)
print("Number:", len(unique_cities))
print("-" * 10)


# Price Report

print("2. Price Report")
prices = {
    "Bread": 50, "Onion": 80, "Eggs": 20, "Tomato": 40, "Coffee": 400
}

for item in prices.items():
    print(f"{item} ETB")
print("-" * 10)


# Tax comprehension

print("3. Tax comprehension")
prices = [100, 250, 400, 80]
total = [p * 1.15 for p in prices]
print(total)
print("-" * 10)


# Cheap items

print ("3. Cheap Items")
cheap = [p for p in prices if p < 200]
print(cheap)
print("-" * 10)

#Write & Read

print("6. Write and Read Names")

with open("names.txt", "w") as f:
    f.write("Eyosiays \n Lidia \n Yoseph")
    
with open("names.txt", "r") as f:
    for line in f:
        print(line.strip())
        
print("-" * 10)


# Safe division

print("6. Safe Division")

try:
    num = int(input("Enter a number:"))
    result = 1000 / num
except ValueError:
    print("Please inter a valid integer")
except ZeroDivisionError:
    print("It can not be divided by zero")
else:
    print(f"1000 divided by {num} is {result}")
finally: 
    print("Division attempt finished")
    
print("-" * 10)