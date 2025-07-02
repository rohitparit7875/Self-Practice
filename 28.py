# Function to print even numbers from 1 to N
def print_even_numbers(n):
    print(f"Even numbers from 1 to {n}:")
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i, end=' ')

# Taking user input
N = int(input("Enter the value of N: "))
print_even_numbers(N)
