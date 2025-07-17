import random

a = random.randint(1, 10)
b = random.randint(1, 10)
answer = int(input(f"What is {a} + {b}? "))

if answer == a + b:
    print("✅ Correct!")
else:
    print(f"❌ Wrong. The answer is {a + b}.")
