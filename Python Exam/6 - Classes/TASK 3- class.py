from person import Person # connection wit class z pliku person.py
class BankAccount():
    def __init__(self, account_number, owner, balance=0):
        self.account_number= account_number
        self.owner= owner
        self. balance= int(balance)

    def deposite(self,add_value):
        self.add_value= add_value
        self.balance = int(self.balance) + int(self.add_value)
        return self.balance
    def withdraw(self,remove_value):
        if remove_value >self.balance:
            return f"No sufficient funds on the account. {self.balance}"
        self. balance= self. balance-int(remove_value)
        return self.balance
    def bank_fees(self, fees):
        self.balance= self. balance - (fees/100*self.balance)
        return self.balance
    def current_balance(self):
        return self.balance

if __name__ == '__main__':
    adam=Person("Adam","KOnieczny",100)
    bank=BankAccount("123-34545",adam,100)
    print(bank.current_balance())
    print(bank.deposite(500))
    print(bank.withdraw(1000))
    print(bank.withdraw(250))
    print(bank.bank_fees(5))
    print(bank.current_balance())



class Bank:
    BANK_FEE = 0.05
    # lista kont


class BankAccount:

    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def __repr__(self):
        return f"{self.owner} {self.account_number} {self.balance}"

    @property
    def current_balance(self):
        return f"Current balance is: {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return self.current_balance

    def withdraw(self, amount):
        if amount > self.balance:
            return f"No sufficient funds on the account. {self.current_balance}"
        self.balance -= amount
        return self.current_balance

    def bank_fees(self):
        self.balance *= 0.95
        return self.current_balance


if __name__ == '__main__':
    adas = Person("Adaś", "Miałczyński", 111111111)
    b = BankAccount(123, adas, 100)
    print(b.current_balance)
    print(b.deposit(500))
    print(b.withdraw(1000))
    print(b.withdraw(250))
    print(b.bank_fees())