import random
import string

def generate_password(length=10):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(random.choice(characters) for _ in range(length))
    print("Generated Password:", password)

generate_password()
