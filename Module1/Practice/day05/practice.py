# 1. Basic Inheritance & super()

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def bonus(self):
        return self.salary * 0.05

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)   
        self.team_size = team_size

    def bonus(self):
        
        return super().bonus() + 1000

print("1. Basic Inheritance & super():")
m = Manager("Almaz", 50000, 4)
print(f"{m.name} bonus: {m.bonus()} ETB")  
print("-" * 40)



# 2. Method Overriding

class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):          
        return "Woof!"

class Cat(Animal):
    def speak(self):          
        return "Meow!"

print("2. Overriding:")
animals = [Dog(), Cat(), Animal()]
for a in animals:
    print(a.speak())
print("-" * 40)



# 3. Polymorphism in Action

def animal_chorus(animals):
    for animal in animals:
        print(animal.speak())

print("3. Polymorphism:")
animal_chorus([Dog(), Cat()])
print("-" * 40)



# 4. Abstract Base Class & @abstractmethod

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def max_speed(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

class Car(Vehicle):
    def max_speed(self):
        return 200

    def fuel_type(self):
        return "Petrol"

class ElectricScooter(Vehicle):
    def max_speed(self):
        return 25

    def fuel_type(self):
        return "Electric"

print("4. Abstract Base Class:")
c = Car()
e = ElectricScooter()
print(f"Car speed: {c.max_speed()} km/h, fuel: {c.fuel_type()}")
print(f"Scooter speed: {e.max_speed()} km/h, fuel: {e.fuel_type()}")
print("-" * 40)



# 5. Composition 


class TransactionHistory:
    def __init__(self):
        self._transactions = []

    def add(self, record):
        self._transactions.append(record)

    def last(self):
        return self._transactions[-1] if self._transactions else None

class AccountWithHistory:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = TransactionHistory()   # composed object

    def deposit(self, amount):
        self.balance += amount
        self.history.add(f"+{amount}")

# Demonstrate composition
print("5. Composition:")
a = AccountWithHistory("Dawit", 1000)
a.deposit(500)
print(f"Balance: {a.balance}, Last transaction: {a.history.last()}")
print("-" * 40)



# 6. Multiple levels of inheritance & method resolution

class A:
    def who(self):
        return "A"

class B(A):
    def who(self):
        return "B"

class C(A):
    def who(self):
        return "C"

class D(B, C):   
    pass

print("6. Multiple Inheritance (MRO):")
d = D()
print(f"D says: {d.who()}")   
print(f"MRO: {[cls.__name__ for cls in D.__mro__]}")