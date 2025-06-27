def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False  # Numbers less than 2 are not prime
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False  # Divisible by another number, not prime
    
    return True  # Prime number

# Test the function
number = 29
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
