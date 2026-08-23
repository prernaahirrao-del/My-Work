import csv

Employee = [
    ["ID " , "Room"],
    ["11" , "Room 201"],
    ["13" , "Room 304"],
    ["12" , "Room 105"]
]

with open("Employee.csv" , "w")as file:
    writer = csv.writer(file)
    writer.writerows(Employee)