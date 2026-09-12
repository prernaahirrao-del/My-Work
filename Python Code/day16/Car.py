class Car:

    def __init__(self , brand , model , price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Price:",self.price)

car1 = Car("Maruti Suzuki","Swift","5.84 lakh")
car2 = Car("Hyundai","i20","6.00 lakh")
car3 = Car("Tata","Nexon","7.40 lakh")

car1.display()
car2.display()
car3.display()
        
        