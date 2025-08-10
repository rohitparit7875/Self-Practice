def is_palindrome(word):
    return word == word[::-1]

text = input("Enter a word: ")
if is_palindrome(text.lower()):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
