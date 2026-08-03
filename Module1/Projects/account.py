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
        print(f"{self.owner} ({self.account_number}): {self.balance:.2f} ETB")

    def _adjust_balance(self, delta):
        self._Account__balance += delta




class SavingsAccount(Account):

    def __init__(self, owner, account_number, balance=0, rate=0.05):
        super().__init__(owner, account_number, balance)
        self.rate = rate

    def add_interest(self):
        interest = self.balance * self.rate
        self.deposit(interest)
        print(f"Interest of {interest:.2f} ETB applied to {self.account_number}")

    def statement(self):
        print(f"[Savings] {self.owner} ({self.account_number}): "
              f"{self.balance:.2f} ETB | rate: {self.rate*100:.1f}%")





class CurrentAccount(Account):

    def __init__(self, owner, account_number, balance=0, overdraft=1000):
        super().__init__(owner, account_number, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if self.balance - amount < -self.overdraft:
            raise ValueError(f"Overdraft limit exceeded (max {self.overdraft} ETB)")
        self._adjust_balance(-amount)
        print(f"Withdrew {amount} ETB from {self.account_number} "
              f"(overdraft allowed)")

    def statement(self):
        print(f"[Current] {self.owner} ({self.account_number}): "
              f"{self.balance:.2f} ETB | overdraft limit: {self.overdraft} ETB")



if __name__ == "__main__":
    
    bank = [
        SavingsAccount("Almaz Bekele", "CBE-1001", 1500, 0.05),
        CurrentAccount("Dawit Tesfaye", "CBE-1002", 800, 1000),
        SavingsAccount("Hanna Alemu", "CBE-1003", 3000, 0.04),
        CurrentAccount("Tigist Mengistu", "CBE-1004", 200, 500),
    ]

    print("=== Account Statements ===")
    for acc in bank:
        acc.statement()                     

    print("\n=== Applying Interest (Savings only) ===")
    for acc in bank:
        if isinstance(acc, SavingsAccount):
            acc.add_interest()

    print("\n=== After Interest ===")
    for acc in bank:
        acc.statement()

    print("\n=== Testing Overdraft ===")
    bank[1].withdraw(1500)   
    bank[1].statement()

    
    try:
        bank[0].balance = -999
    except AttributeError as e:
        print(f"Protected: {e}")