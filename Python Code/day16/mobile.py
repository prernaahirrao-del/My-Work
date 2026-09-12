class Mobile:

    def __init__(self , brand , price):
        self.brand = brand
        self.price = price

    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)

    def discount(self):
        discount = self.price * 10/100
        final_price = self.price - discount
        print("After 10% Discount:",final_price)

mobile1 = Mobile("iPhone18",250000)

mobile1.display()
mobile1.discount()
