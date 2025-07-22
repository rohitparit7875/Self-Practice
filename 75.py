# Program to count words without using inbuilt functions

# Take input from user
sentence = input("Enter a sentence: ")

word_count = 0
in_word = False

for char in sentence:
    if char != ' ' and not in_word:
        word_count += 1
        in_word = True
    elif char == ' ':
        in_word = False

print(f"Total number of words: {word_count}")