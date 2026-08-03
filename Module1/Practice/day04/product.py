class Product:
    
    def __init__(self, name, price, quantity=0):
        self.name = name         
        self.price = price        
        self.__quantity = quantity  

    @property
    def quantity(self):
        
        return self.__quantity

    def restock(self, amount):
        
        if amount <= 0:
            raise ValueError("Restock amount must be positive")
        self.__quantity += amount

    def sell(self, amount):
        
        if amount <= 0:
            raise ValueError("Sell amount must be positive")
        if amount > self.__quantity:
            raise ValueError(f"Not enough stock. Available: {self.__quantity}")
        self.__quantity -= amount

    def __str__(self):
        return f"{self.name}: {self.price} ETB, {self.quantity} in stock"



if __name__ == "__main__":
    p = Product("Cough Syrup", 45, 20)
    print(p)
    p.sell(5)
    p.restock(10)
    print(f"Updated quantity: {p.quantity}")
   