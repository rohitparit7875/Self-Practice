lst = list(map(int, input("Enter numbers separated by space: ").split()))
if lst == sorted(lst):
    print("The list is sorted")
else:
    print("The list is not sorted")
