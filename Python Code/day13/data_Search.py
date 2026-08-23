import csv

search_id = "101"

with open("student.csv" , "r")as file:

    reader = csv.DictReader(file)
    for row in reader:
        if row["ID"].strip() == search_id:
            print("Studen Found")
            print("Name:",row["Name"])

            print("Marks" , row["Marks"])