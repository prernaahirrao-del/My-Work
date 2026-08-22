search_name = input("Enter Student Name")

file = open("create.txt", "r")

found = False

for name in file:

    if name.strip().lower() == search_name.lower():
        found = True
        break

file.close()

if found:
    print("Student Found")
else:
    print("Student Not Found")