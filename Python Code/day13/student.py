import csv

student = [
    ["id" , "name" , "field" , "marks"] , 
    ["101" , "sonu" , "mechanical" , "70"] , 
    ["102" , "monu" , "Civil" , "75"] ,
    ["103" , "Rosh" , "Computer" , "75"]
]

with open("marks.csv" , "w" , newline="") as file:
    writer = csv.writer(file)

    writer.writerows(student)