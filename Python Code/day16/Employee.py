class Employee:

    def __init__(self , name, employee_id, salary, department):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.department = department

    def display(self):
        print("Name:",self.name)
        print("Employee ID",self.employee_id)
        print("Salary:",self.salary)
        print("Department:",self.department)

employee1 = Employee("Raj","RAM001",45000,"IT")
employee2 = Employee("Sham","RAM001",38000,"Computer")
employee3 = Employee("Ravi","RAM003",52000,"Finance")

employee1.display()
employee2.display()
employee3.display()
        