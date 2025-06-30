def reverse_string(s):
    # Initialize an empty string for the reversed result
    reversed_s = ""
    # Iterate through the original string in reverse order
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

# Input string
string = input("Enter a string to reverse: ")

# Call the function and display the result
print("Reversed string:", reverse_string(string))
