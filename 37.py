# Find second largest number without using sort or max
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

if len(numbers) < 2:
    print("Need at least two numbers.")
else:
    first = second = float('-inf')
    
    for num in numbers:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    if second == float('-inf'):
        print("No second largest found (all numbers may be same).")
    else:
        print("Second largest number is:", second)
