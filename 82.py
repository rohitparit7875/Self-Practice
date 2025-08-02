def is_palindrome(num):
    original = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10

    return original == reversed_num

# Test
print(is_palindrome(121))   # Output: True
print(is_palindrome(123))   # Output: False
