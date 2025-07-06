def is_even(n):
    quotient = n // 2
    product = quotient * 2
    if product == n:
        return True
    else:
        return False

# User input
num = int(input("Enter a number to check if it's even or odd: "))
if is_even(num):
    print(num, "is even.")
else:
    print(num, "is odd.")
