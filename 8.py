string = input("Enter a string: ")
string_lower = string.lower()
if string_lower == string_lower[::-1]:
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")
