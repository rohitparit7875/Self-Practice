import random

words = ['python', 'jumble', 'coding', 'program']
word = random.choice(words)
scrambled = ''.join(random.sample(word, len(word)))

print(f"Unscramble this word: {scrambled}")
guess = input("Your guess: ")

if guess.lower() == word:
    print("Correct!")
else:
    print(f"Wrong! The word was '{word}'.")
