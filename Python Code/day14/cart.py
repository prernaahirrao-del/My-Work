cart = []

while True:

    print("\nShopping Cart")
    print("1 . Add Product")
    print("2 . View Card")
    print("3 . Total Bill")
    print("4 . Exit")

    try:
        choice = int(input("Enter choice :"))

        if choice == 1:

            name = input("Enter product name :")
            price = float(input("Enter price :"))
            quantity = int(input("Enter quantity :"))

            if price <= 0:
                raise ValueError("price must be greater than zero")

            if quantity <= 0:
                raise ValueError("Quantity must be greater than zero")

            item = {
                "name" : name,
                "price" : price,
                "quantity" : quantity
            }

            cart.append(item)

            print("Product added to cart")

        elif choice == 2:

            if len(cart) ==0:
                print("Cart is empty")

            else:
                print("\nYour Cart")

                for item in cart:
                    total = item["price"] * item["quantity"]

                    print("product :",item["name"])
                    print("price :",item["price"])
                    print("quantity :",item["quantity"])
                    print("Total :",total)
                    print("------------------")

        elif choice == 3:

            grand_total = 0

            for item in cart:
                total = item["price"] * item["quantity"]
                grand_total += total

            print("Grand Total =", grand_total)

        elif choice == 4:

             print("Thankyou for Shopping ")
             break
        else:
            print("please select 1 to 4")

    except ValueError as e:
        print("Error :", e)
    finally:
        print("Operation completed")

            