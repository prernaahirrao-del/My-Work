class BankAccount:

    def __init__(self , name , balance):
        self.name = name
        self.balance = balance

    def deposite(self , amount):
        self.balance = self.balance + amount

    def withdraw(self , amount):
        self.balance = self.balance - amount

    def display(self):
        print("Name:",self.name)
        print("balance:",self.balance)

account1 = BankAccount("Rahul",5000)

account1.display()

account1.deposite(3000)

print("After Deposite : ")
account1.display()

account1.withdraw(1000)

print("After Withdraw : ")
account1.display()