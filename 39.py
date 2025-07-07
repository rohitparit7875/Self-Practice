# Count alphabets, digits, and special characters
text = input("Enter a string: ")

alphabets = digits = specials = 0

for char in text:
    if char.isalpha():
        alphabets += 1
    elif char.isdigit():
        digits += 1
    else:
        specials += 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Special Characters:", specials)
