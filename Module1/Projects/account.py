from collections import deque


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
        self.history = []                  

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        self.history.append(('deposit', amount))
        self._notify(f"Deposit +{amount} ETB → balance {self.balance} ETB")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        self.history.append(('withdraw', amount))
        self._notify(f"Withdrawal -{amount} ETB → balance {self.balance} ETB")

    def undo_last(self):
        
        if not self.history:
            print("Nothing to undo")
            return
        action, amount = self.history.pop()
        if action == 'deposit':
            self.__balance -= amount
            self._notify(f"Undo deposit -{amount} ETB → balance {self.balance} ETB")
        elif action == 'withdraw':
            self.__balance += amount
            self._notify(f"Undo withdrawal +{amount} ETB → balance {self.balance} ETB")

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
        self.history.append(('withdraw', amount))
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



class AccountRegistry:
    def __init__(self):
        self.by_number = {}
        self.order = []
        self.pending_transfers = deque()

    def add(self, acc):
        self.by_number[acc.account_number] = acc
        self.order.append(acc.account_number)

    def find(self, number):
        return self.by_number.get(number)   

    def list_all(self):
        return [self.by_number[num] for num in self.order]

    def transfer_request(self, from_num, to_num, amount):
        
        self.pending_transfers.append((from_num, to_num, amount))
        print(f"Queued transfer: {from_num} → {to_num}, {amount} ETB")

    def process_transfers(self):
        
        while self.pending_transfers:
            from_num, to_num, amount = self.pending_transfers.popleft()
            from_acc = self.find(from_num)
            to_acc = self.find(to_num)
            if not from_acc or not to_acc:
                print(f"Transfer failed: invalid account(s) in {from_num}→{to_num}")
                continue
            try:
                from_acc.withdraw(amount)
                to_acc.deposit(amount)
                print(f"Transferred {amount} ETB from {from_num} to {to_num}")
            except ValueError as e:
                print(f"Transfer failed: {e}")



if __name__ == "__main__":
    reg = AccountRegistry()

    
    a1 = AccountFactory.create("savings", "Almaz Bekele", "CBE-1001", 1500)
    a2 = AccountFactory.create("current", "Dawit Tesfaye", "CBE-1002", 800)
    reg.add(a1)
    reg.add(a2)

    
    a1.subscribe(SMSAlert())

    print("=== Initial Statements ===")
    for acc in reg.list_all():
        acc.statement()

    
    print("\n=== Transactions ===")
    a1.deposit(500)
    a1.withdraw(200)
    a2.withdraw(300)


    print("\n=== History (a1) ===")
    print(a1.history)


    print("\n=== Undo Last (a1) ===")
    a1.undo_last()
    a1.statement()

    print("\n=== O(1) Lookup ===")
    acc = reg.find("CBE-1002")
    if acc:
        acc.statement()

   
    print("\n=== Pending Transfers ===")
    reg.transfer_request("CBE-1002", "CBE-1001", 100)
    reg.transfer_request("CBE-1001", "CBE-1002", 50)
    reg.process_transfers()

    print("\n=== After Transfers ===")
    for acc in reg.list_all():
        acc.statement()