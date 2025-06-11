# Function to calculate the sum of all numbers in a list
def sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Taking user input
numbers_list = []
n = int(input("Enter the number of elements in the list: "))

print("Enter the numbers one by one:")
for _ in range(n):
    number = int(input())
    numbers_list.append(number)

# Call the function and print the result
result = sum(numbers_list)
print("The sum of all numbers in the list is:", result)
