# Take input from the user
user_input = input("Enter a string: ")

# Initialize an empty string for the reversed result
reversed_string = ""

# Loop through the string in reverse order
for char in user_input:
    reversed_string = char + reversed_string

# Print the reversed string
print("Reversed string:", reversed_string)
