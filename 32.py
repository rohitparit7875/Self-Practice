def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# GCD Calculation
gcd = find_gcd(num1, num2)

# Output
print(f"The GCD of {num1} and {num2} is {gcd}")
