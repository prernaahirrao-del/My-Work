text = "Roshani"
Char_Count = {}

for char in text :
    if char in Char_Count:
        Char_Count[char] += 1
    else:
        Char_Count[char] = 1
print("Character Frequencies:", Char_Count)