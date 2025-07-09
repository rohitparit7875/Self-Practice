def is_perfect_square(n):
    i = 1
    while i * i <= n:
        if i * i == n:
            return True
        i += 1
    return False

def print_perfect_squares(start, end):
    print(f"Perfect squares between {start} and {end}:")
    for i in range(start, end + 1):
        if is_perfect_square(i):
            print(i, end=' ')

# Input from user
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
print_perfect_squares(start, end)
