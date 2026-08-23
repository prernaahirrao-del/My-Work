import csv

search_id = input("Enter the Student Id:").strip()

gpas = []
found_student  = None
with open("STD.csv" , "r")as file:
    reader = csv.DictReader(file)

    for row in reader:
        gpa = float(row["GPA"])
        gpas.append(gpa)

        if row["ID"].strip() == search_id:
            found_student = row

class_avg = sum(gpas) / len(gpas)
print(f"Class Average GPA:{class_avg:2f}\n")

if found_student:
    student_gpa = float(found_student["GPA"])
    print(f"Found:{found_student['Name']}")
    print(f"GPA:{student_gpa}")

    if student_gpa >= class_avg:
        print("Status: Above Average")
    else:
        print("Status: Below Average")
else:
    print("Student ID not found")