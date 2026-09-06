import shopping

product = input("Enter the product name :")
price = int(input("Enter the product price :"))
quantity = int(input("Enter the quantity :"))

print("total",shopping.product_bill(price,quantity))