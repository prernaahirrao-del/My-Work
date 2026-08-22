Cart = {
    "5 course meal" : 899,
    "Chickan Burst" : 499,
    "Big veg Pizza" : 999,
    "Veg Pizza"     : 280,
    "Garlic Bread"  : 399
}

item = "Chickan Burst"
quantity = 4
if item in Cart:
    Total_cost = Cart[item]*quantity
    print(f"Cost for {quantity} X {item}:{Total_cost}")
else:
    print("Item is not existed")


