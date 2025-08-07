def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

# Example usage
for num in fibonacci(100):
    print(num, end=' ')
