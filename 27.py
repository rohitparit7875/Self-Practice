# Fibonacci Series up to n terms

def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci series:")
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Example usage
terms = int(input("Enter the number of terms: "))
fibonacci(terms)
