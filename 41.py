nums = list(map(int, input("Enter numbers separated by space: ").split()))
pos = neg = zero = 0
for n in nums:
    if n > 0:
        pos += 1
    elif n < 0:
        neg += 1
    else:
        zero += 1
print(f"Positive: {pos}, Negative: {neg}, Zeros: {zero}")
