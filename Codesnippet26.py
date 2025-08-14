s = input("Enter a word: ").strip()
print("Palindrome" if s == s[::-1] else "Not a palindrome")
