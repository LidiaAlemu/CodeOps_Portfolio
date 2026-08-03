from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self._balance = balance      

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def statement(self):
        print(f"{self.owner} ({self.account_number}): {self.balance:.2f} ETB "
              f"[{self.account_type()}]")

    @abstractmethod
    def account_type(self):
        pass



class BusinessAccount(Account):
    def __init__(self, owner, account_number, balance=0,
                 interest_rate=0.07, min_balance=1000):
        super().__init__(owner, account_number, balance)
        self.interest_rate = interest_rate
        self.min_balance = min_balance

    def account_type(self):
        return "Business"

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Business interest of {interest:.2f} ETB applied")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if self.balance - amount < self.min_balance:
            raise ValueError(f"Cannot go below minimum balance of {self.min_balance} ETB")
        super().withdraw(amount)   



if __name__ == "__main__":
    ba = BusinessAccount("Tigist & Co.", "BUS-0001", 5000, 0.07, 2000)
    ba.statement()
    ba.add_interest()
    ba.statement()
    try:
        ba.withdraw(4000)   
    except ValueError as e:
        print(f"Blocked: {e}")
    ba.statement()