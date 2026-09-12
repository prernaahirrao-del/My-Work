class Student:

    def __init__(self , name , age , course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Course:",self.course)

student1 = Student("Rahul",20,"Python")
student2 = Student("Amit",21,"Java")
student3 = Student("Priya",19,"Python")

student1.display()
student2.display()
student3.display()