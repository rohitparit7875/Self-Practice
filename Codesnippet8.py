import random

number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("🎉 Correct! You guessed the number!")
else:
    print(f"❌ Wrong! The number was {number}")
