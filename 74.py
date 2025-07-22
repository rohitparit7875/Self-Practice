import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# User gets 3 chances to guess
for attempt in range(3):
    guess = int(input("Guess a number between 1 and 10: "))
    
    if guess == secret_number:
        print("🎉 Correct! You guessed the number!")
        break
    else:
        print("❌ Wrong guess. Try again.")

if guess != secret_number:
    print(f"Game Over! The number was {secret_number}.")