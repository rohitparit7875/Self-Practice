def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print("Factorial of 5:", factorial(5))
print("Factorial of 0:", factorial(0))
