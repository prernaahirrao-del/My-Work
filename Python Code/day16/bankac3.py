class BankAccount:

    def __init__(self , name , balance):
        self.name = name
        self.balance = balance

    def deposite(self,amount):
        self.balance = self.balance+amount
        print("Account Deposite:",amount)

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount Withdraw:",amount)
        else:
            print("Insufficient balance")

    def display(self):
        print("Account Holder:",self.name)
        print("Balance:",self.balance)

account1 = BankAccount("Rahul",5000)

account1.display()

print("\nDeposite:")
account1.deposite(2000)
account1.display()

print("\nWithdraw:")
account1.withdraw(3000)
account1.display()

print("\nWithdraw:")
account1.withdraw(1000)
account1.display()





      
    

    