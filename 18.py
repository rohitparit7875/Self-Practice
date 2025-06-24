# Function to reverse a string without inbuilt functions
def reverse_string(input_string):
    reversed_str = ""
    for char in input_string:
        reversed_str = char + reversed_str
    return reversed_str


# Take input from the user
user_input = input("Enter a string to reverse: ")
reversed_string = reverse_string(user_input)

print("Original string:", user_input)
print("Reversed string:", reversed_string)
