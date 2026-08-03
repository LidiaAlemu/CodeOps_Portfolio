class Account:
    
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner                  
        self.account_number = account_number  
        self.__balance = balance            

    @property
    def balance(self):
        
        return self.__balance

    def deposit(self, amount):
        
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    def statement(self):
        
        print(f"{self.owner} ({self.account_number}): {self.balance} ETB")



if __name__ == "__main__":
    acc1 = Account("Almaz Bekele", "CBE-1001", 1500)
    acc2 = Account("Dawit Tesfaye", "CBE-1002", 800)

    acc1.deposit(500)
    acc1.withdraw(200)
    acc1.statement()          

    
    try:
        acc1.balance = -999
    except AttributeError as e:
        print(f"Protected: {e}")   

    
    try:
        acc2.withdraw(2000)
    except ValueError as e:
        print(f"Validation works: {e}")   

    
    print(f"Acc1 balance: {acc1.balance}, Acc2 balance: {acc2.balance}")