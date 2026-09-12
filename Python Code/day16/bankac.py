class BankAccount:

    def __init__(self, name ,balance):
        self.name = name
        self.balance = balance

    def display(self):
         print("Account Holder:", self.name)
         print("Balance:", self.balance)

    def deposite(self , amount):
         self.balance = self.balance + amount


account1 = BankAccount("Rahul" , 5000)

account1.display()

account1.deposite(2000)

print("\nAfter Deposite:")
account1.display()

