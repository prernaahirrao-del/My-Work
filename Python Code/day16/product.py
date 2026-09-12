class Product:

    def __init__(self , name , price ,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price*self.quantity

    def display(self):
        print("Product:",self.name)
        print("Price:",self.price)
        print("Quantity:", self.quantity)
        print("Total:",self.total())

p1 = Product("Keyboard",800,2)
p2 = Product("Mouse",500,3)

p1.display()

print()

p2.display()
    