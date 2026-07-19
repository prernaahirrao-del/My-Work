Account_balance = 30000
Account_pin = 8482

print("ATM")
enter_pin = float(input("enter the 4 digit pin :"))
if Account_pin == enter_pin:
    print("Entered pin successfully")
    withdraw_amount = float(input("enter the amount :"))
    if withdraw_amount <= Account_balance:
        Account_balance -= withdraw_amount
        print (f"cash withdraw successfull: {withdraw_amount}")
        print(f"total account balance: {Account_balance}")
    else:
        print("balance low cant withdrawl")
else:
    print("Invalid Pin")