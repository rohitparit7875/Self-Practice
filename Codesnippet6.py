num = int(input("Enter a number: "))

while num >= 10:   # Keep summing until single digit
    sum_digits = 0
    for digit in str(num):
        sum_digits += int(digit)
    num = sum_digits

print("Single digit sum is:", num)
