try:
    age = int(input("Enter the Age"))

    if age < 0 :                                             
        raise ValueError("Age cannot be negetive")
    elif age >= 18:
     print("You are an adult")
    else:
        print("You are minor")

    print("Your age is:", age)

except ValueError as e:
    print("Invalid input:" , e)

