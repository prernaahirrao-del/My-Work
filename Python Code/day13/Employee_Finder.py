import csv

search_room = "13"

with open("Employee.csv" , "r")as file:

    reader = csv.DictReader(file)

    for row in reader:
        if row["ID"].strip() == search_room:
            print("Employee Room Find")
            print("ID:" , row["ID"] )

            print("Room:", row["Room"])

