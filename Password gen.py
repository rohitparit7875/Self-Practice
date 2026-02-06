import random
import string

length = 8
chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(chars) for _ in range(length))

print("Generated Password:", password)
