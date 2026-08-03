# 1. Book class with describe()

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"

book1 = Book("The River Between", "Ngũgĩ wa Thiong'o", 152)
book2 = Book("Cutting for Stone", "Abraham Verghese", 667)
print("1. Books:")
print(book1.describe())
print(book2.describe())
print("-" * 10)



# 2. Product class with restock() and sell()

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price          
        self.quantity = quantity

    def restock(self, n):
        if n <= 0:
            print("Restock amount must be positive")
            return
        self.quantity += n
        print(f"Restocked {self.name}: +{n} → {self.quantity} units")

    def sell(self, n):
        if n <= 0:
            print("Sell amount must be positive")
            return
        if n > self.quantity:
            print(f"Not enough stock of {self.name} (available: {self.quantity})")
            return
        self.quantity -= n
        print(f"Sold {n} {self.name} → {self.quantity} left")

print("2. Product class (public attributes):")
paracetamol = Product("Paracetamol", 5, 100)
paracetamol.sell(20)
paracetamol.restock(50)
print("-" * 10)



# 3. Make it private  __quantity with @property getter

class ProductEncapsulated:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity      

    @property
    def quantity(self):
        
        return self.__quantity

    def restock(self, n):
        if n <= 0:
            raise ValueError("Restock amount must be positive")
        self.__quantity += n

    def sell(self, n):
        if n <= 0:
            raise ValueError("Sell amount must be positive")
        if n > self.__quantity:
            raise ValueError("Insufficient stock")
        self.__quantity -= n

print("3. Private quantity with @property:")
amox = ProductEncapsulated("Amoxicillin", 12, 30)
print(f"Quantity: {amox.quantity}")   
try:
    amox.quantity = 100   
except AttributeError as e:
    print(f"Protected: {e}")
print("-" * 10)



# 4. Validate refuse negative quantity (guard in sell)


print("4. Validation:")
p = ProductEncapsulated("Bandages", 15, 10)
try:
    p.sell(15)
except ValueError as e:
    print(f"Caught: {e}")   
print(f"After failed sale: {p.quantity} (should still be 10)")
print("-" * 10)



# 5. Prove independence three objects, change one

print("5. Independence:")
p1 = ProductEncapsulated("A", 10, 5)
p2 = ProductEncapsulated("B", 20, 8)
p3 = ProductEncapsulated("C", 30, 12)

p1.sell(2)         
p2.restock(3)       

print(f"p1 quantity: {p1.quantity}") 
print(f"p2 quantity: {p2.quantity}")  
print(f"p3 quantity: {p3.quantity}")  