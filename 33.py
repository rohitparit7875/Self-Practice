def is_perfect(n):
    if n < 2:
        return False

    sum_of_divisors = 1  # 1 is always a proper divisor
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            sum_of_divisors += i

    return sum_of_divisors == n

# Input from user
num = int(input("Enter a number: "))

# Check and display result
if is_perfect(num):
    print(f"{num} is a Perfect Number ✅")
else:
    print(f"{num} is NOT a Perfect Number ❌")
