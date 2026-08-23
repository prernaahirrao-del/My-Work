import csv

with open("student.csv" , "w" , newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["ID" , "Name" , "Branch" , "Marks"])
    writer.writerow(["101" , "Prerna" , "Computer" , "82"])
    writer.writerow(["102" , "Roshani" , "IT" , "85"])
    writer.writerow(["103" , "kajal" , "Computer" , "72"])

print("CSv file created successfully")