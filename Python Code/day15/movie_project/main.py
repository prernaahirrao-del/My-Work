import movie
import booking
import validation

def main():

    cart = []

    while True:

        print("\n====================")
        print("SHOP BILLING")
        print("======================")

        print("1 . Add Product")
        print("2 . Dsiplay Product")
        print("3 . Create Bill")
        print("4 . Exit")

        choice = input("Enter choice: ")

        try:

            if choice == "1":

                name = input("Enter product name:")

                validation.validate_name(name)

                price = float(
                    input("Enter price :")
                )

                quantity = int(
                    input("Enter quantity:")
                )

                validation.validate_price(price)
                validation.validate_quantity(quantity)

                product.add_product(
                    name,
                    price,
                    quantity
                )
                print("Product added successfully")