#project on Reverse number
target_num = int(input("Enter the 3 digit number (for eg.256) :"))

unit_digit = target_num % 10
droped_factor = target_num // 10
tens_digit = droped_factor % 10
hundred_digit = droped_factor // 10

reverse_value = (unit_digit*100)+ (tens_digit *10) + hundred_digit

print(f"target_value : {target_num}")
print(f"Inverted value : {reverse_value}")