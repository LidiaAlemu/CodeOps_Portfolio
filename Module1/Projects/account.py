class BankConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.interest_rate = 0.05
            cls._instance.overdraft_limit = 1000
        return cls._instance


class Account:

    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance          
        self._observers = []

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        self._notify(f"Deposit +{amount} ETB → balance {self.balance} ETB")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        self._notify(f"Withdrawal -{amount} ETB → balance {self.balance} ETB")

    def statement(self):
        print(f"{self.owner} ({self.account_number}): {self.balance:.2f} ETB")

    def _adjust_balance(self, delta):
        self._Account__balance += delta

    def subscribe(self, observer):
        self._observers.append(observer)

    def _notify(self, event):
        for observer in self._observers:
            observer.update(event)


class SavingsAccount(Account):

    def __init__(self, owner, account_number, balance=0, rate=None):
        super().__init__(owner, account_number, balance)
        self.rate = rate if rate is not None else BankConfig().interest_rate

    def add_interest(self):
        interest = self.balance * self.rate
        self.deposit(interest)
        print(f"Interest of {interest:.2f} ETB applied to {self.account_number}")

    def statement(self):
        print(f"[Savings] {self.owner} ({self.account_number}): "
              f"{self.balance:.2f} ETB | rate: {self.rate*100:.1f}%")


class CurrentAccount(Account):

    def __init__(self, owner, account_number, balance=0, overdraft=None):
        super().__init__(owner, account_number, balance)
        self.overdraft = overdraft if overdraft is not None else BankConfig().overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if self.balance - amount < -self.overdraft:
            raise ValueError(f"Overdraft limit exceeded (max {self.overdraft} ETB)")
        self._adjust_balance(-amount)
        self._notify(f"Withdrawal -{amount} ETB (overdraft) → balance {self.balance} ETB")

    def statement(self):
        print(f"[Current] {self.owner} ({self.account_number}): "
              f"{self.balance:.2f} ETB | overdraft limit: {self.overdraft} ETB")


class AccountFactory:
    @staticmethod
    def create(kind, owner, number, balance=0):
        if kind == "savings":
            return SavingsAccount(owner, number, balance)
        if kind == "current":
            return CurrentAccount(owner, number, balance)
        raise ValueError(f"Unknown account type: {kind}")


class SMSAlert:
    def update(self, event):
        print(f"[TeleBirr SMS] {event}")


class AuditLog:
    def update(self, event):
        print(f"[Audit Log] {event}")


if __name__ == "__main__":
    config1 = BankConfig()
    config2 = BankConfig()
    print(f"Same config? {config1 is config2}")

    acc1 = AccountFactory.create("savings", "Almaz Bekele", "CBE-1001", 1500)
    acc2 = AccountFactory.create("current", "Dawit Tesfaye", "CBE-1002", 800)

    acc1.subscribe(SMSAlert())
    acc1.subscribe(AuditLog())
    acc2.subscribe(AuditLog())

    print("\n--- Transactions ---")
    acc1.deposit(500)
    acc1.withdraw(200)
    acc2.withdraw(1500)

    print("\n--- Statements ---")
    acc1.statement()
    acc2.statement()