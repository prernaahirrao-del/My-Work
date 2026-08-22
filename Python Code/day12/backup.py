source = open("create.txt" , "r")
data = source.read()

source.close()
destination = open("backup.txt" , "w")
destination.write(data)
destination.close()
print("your file copy successfully")