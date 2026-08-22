numbers = [25,12,45,8,32]
smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest =",smallest)