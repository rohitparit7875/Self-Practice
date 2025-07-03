def count_vowels_consonants(s):
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    capital_vowels = ['A', 'E', 'I', 'O', 'U']

    vowels = 0
    consonants = 0

    i = 0
    while i < len(s):
        ch = s[i]

        # Check if character is a letter (A-Z or a-z)
        if ('A' <= ch and ch <= 'Z') or ('a' <= ch and ch <= 'z'):
            # Check if vowel
            found = False
            j = 0
            while j < 5:
                if ch == vowels_list[j] or ch == capital_vowels[j]:
                    vowels += 1
                    found = True
                    break
                j += 1
            if not found:
                consonants += 1
        i += 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)

# Example usage
input_str = "Hello World!"
count_vowels_consonants(input_str)
