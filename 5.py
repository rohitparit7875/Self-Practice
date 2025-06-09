def is_palindrome_num(n):
    temp = n
    rev = 0

    # Reverse the number without using strings
    while temp > 0:
        d = temp % 10  # Extract the last digit
        rev = rev * 10 + d  # Build the reversed number
        temp = temp // 10  # Remove the last digit

    # Compare the original number with the reversed number
    return n == rev

# Input from user
num = int(input("Enter a number to check if it's a palindrome: "))

# Check and display result
if is_palindrome_num(num):
    print(f"{num} is a palindrome!")
else:
    print(f"{num} is not a palindrome.")
