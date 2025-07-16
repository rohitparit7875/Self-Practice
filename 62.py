def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

print("Is 'madam' a palindrome?", is_palindrome("madam"))
print("Is 'Hello' a palindrome?", is_palindrome("Hello"))
