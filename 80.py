def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

nums = [5, 3, 8, 1, 2]
print("Original list:", nums)
sorted_nums = bubble_sort(nums)
print("Sorted list:", sorted_nums)
