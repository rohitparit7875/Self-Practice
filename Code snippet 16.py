def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Example usage
print(is_palindrome("Racecar"))
