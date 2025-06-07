def fib_seq(n):
    """Generate a Fibonacci sequence of n terms."""
    if n <= 0:
        print("Please enter a positive integer.")
        return
    elif n == 1:
        print("Fibonacci sequence: 0")
        return
    elif n == 2:
        print("Fibonacci sequence: 0, 1")
        return
   
    a, b = 0, 1
    print("Fibonacci sequence:", end=" ")
    print(a, b, end=" ")
  
    for _ in range(2, n):
        c = a + b
        print(c, end=" ")
        a, b = b, c

n = int(input("Enter the number of terms in the Fibonacci sequence: "))

fib_seq(n)
