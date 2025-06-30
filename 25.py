# Swapping using a temporary variable
def swap_with_temp(a, b):
    print(f"Before swapping: a = {a}, b = {b}")
    temp = a
    a = b
    b = temp
    print(f"After swapping: a = {a}, b = {b}")

# Input two numbers
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

swap_with_temp(a, b)
