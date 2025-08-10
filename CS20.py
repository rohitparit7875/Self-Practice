import random

secret = random.randint(1, 10)
guess = int(input("Guess the number (1-10): "))

if guess == secret:
    print("🎉 Correct!")
else:
    print(f"❌ Wrong! The number was {secret}")
