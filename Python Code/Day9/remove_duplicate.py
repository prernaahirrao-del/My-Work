numbers  = [10,20,30,40,50,20,40,30,10,50]
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)