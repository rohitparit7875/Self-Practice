numbers = list(map(int, input("Enter numbers separated by space: ").split()))
unique_numbers = list(set(numbers))
unique_numbers.sort(reverse=True)

if len(unique_numbers) >= 2:
    print("Second largest number:", unique_numbers[1])
else:
    print("Not enough unique numbers")
