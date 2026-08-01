order = ["Chikan Wings","Chikan Burst Burger","Fries"]
item_price = [300,250,100]

Total = sum(item_price)
print("---------KFC---------")
for i in range(len(order)):
    print(f"{order[i]}: {item_price[i]}")

print("-------------------")
print(f"Total Amount:{Total}")