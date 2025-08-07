def is_palindrome_number(num):
    original = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    return original == reversed_num

# Example
print(is_palindrome_number(121))  # True
print(is_palindrome_number(123))  # False
