import csv

new = [104 , "Neha" , "Civil" , 80]

with open("student.csv" , "a" , newline="")as file:

    writer = csv.writer(file)
    writer.writerow(new)
