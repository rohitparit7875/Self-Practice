# Function to calculate the sum of digits
def sum_of_digits(number):
    # Convert the number to positive if it's negative
    number = abs(number)
    total = 0

    while number > 0:
        digit = number % 10  # Get the last digit
        total += digit       # Add the digit to the total
        number //= 10        # Remove the last digit

    return total

# Take input from the user
num = int(input("Enter a number: "))

# Call the function and display the result
print("Sum of the digits:", sum_of_digits(num))
