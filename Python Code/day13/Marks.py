import csv

with open("student.csv" ,"r")as file:
    reader = csv.DictReader(file)

    for row in reader:
        if int(row["Marks"]) > 80:
            print(row["Name"] , row["Marks"])

