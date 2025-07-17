import random

guess = input("Heads or Tails? ").lower()
flip = random.choice(["heads", "tails"])

if guess == flip:
    print("🎉 You guessed right!")
else:
    print(f"❌ Wrong! It was {flip}.")
