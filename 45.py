def is_digit(char):
    return char >= '0' and char <= '9'

def mask_digits(text):
    result = ""
    for ch in text:
        if is_digit(ch):
            result += '*'
        else:
            result += ch
    print("Masked string:", result)

# Input from user
user_input = input("Enter a string with numbers: ")
mask_digits(user_input)
