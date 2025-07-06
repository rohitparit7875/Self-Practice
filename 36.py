def is_armstrong(n):
    original = n
    total = 0
    while n > 0:
        digit = n % 10
        cube = digit * digit * digit
        total += cube
        n = n // 10
    return total == original

# User input
num = int(input("Enter a 3-digit number to check if it's Armstrong: "))
if 100 <= num <= 999:
    if is_armstrong(num):
        print(num, "is an Armstrong number.")
    else:
        print(num, "is not an Armstrong number.")
else:
    print("Please enter a 3-digit number.")
