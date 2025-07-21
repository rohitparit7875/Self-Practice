def is_palindrome(word):
    return word == word[::-1]

words = ["madam", "hello", "noon", "world", "civic"]
palindromes = list(filter(is_palindrome, words))
print("Palindromes in list:", palindromes)
