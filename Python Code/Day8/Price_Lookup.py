price = {

    "Paneer Pizza" : 290,
    "Vegie Pizza" : 190,
    "Chikan Pizza" : 360,
    "Margerita Pizza" : 200,
}

item = "Margerita Pizza"
quantity = 2
if item in price:
    total_cost = price[item]*quantity
    print(f"cost for {quantity} X {item} : {total_cost}")

else:
    print("Items not found")    