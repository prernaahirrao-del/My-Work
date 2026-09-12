class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def Display(self):
        print("Name",self.name)
        print("Age",self.age)

student1 = Student("Prerna",21)
student2 = Student("Roshani",22)

student1.Display()
student2.Display()
        