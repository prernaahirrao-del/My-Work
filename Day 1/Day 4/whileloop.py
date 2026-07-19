Correct_Pin = "8482"
user_input = ""

while user_input != Correct_Pin:
    user_input = input("Enter the 4 Digit Pin :")   
    if user_input != Correct_Pin:
        print("Access Denied/Try Again.\n")

print("Access Granted Welcome!!!!")

