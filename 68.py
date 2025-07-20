numbers = list(map(int, input("Enter numbers separated by space: ").split()))
even_count = sum(1 for n in numbers if n % 2 == 0)
odd_count = len(numbers) - even_count

print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")
