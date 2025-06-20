# Function to count vowels in a string
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0

    for char in input_string:
        if char in vowels:
            count += 1

    return count

# Take input from the user
user_input = input("Enter a string: ")

# Call the function and display the result
print("Number of vowels:", count_vowels(user_input))
