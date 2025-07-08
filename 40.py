char = input("Enter a single alphabet: ")

if len(char) == 1 and char.isalpha():
    if char.lower() in 'aeiou':
        print("It's a vowel.")
    else:
        print("It's a consonant.")
else:
    print("Please enter a valid single alphabet.")
