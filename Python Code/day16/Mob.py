class Mobile:

    def __init__(self , brand , model , price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("Brand :",self.brand)
        print("Model:",self.model)
        print("Price:",self.price)

mobile1 = Mobile("Apple","iphone17 pro max",165900)
mobile2 = Mobile("Sansung","Samsung S23 Ultra",159999)
mobile3 = Mobile("Google","Pixel 10 pro XL",124000)

mobile1.display()
mobile2.display()
mobile3.display()
        