def has_unique_characters(string):
    # Use a set to track characters we've seen
    seen = set()
    for char in string:
        if char in seen:
            return False  # Duplicate found
        seen.add(char)
    return True  # No duplicates found

# Input from the user
user_input = input("Enter a string to check for unique characters: ")

# Check and display the result
if has_unique_characters(user_input):
    print("The string has all unique characters.")
else:
    print("The string does not have all unique characters.")
