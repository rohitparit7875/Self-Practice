def bubble_sort(arr):
    """
    Sorts the input array using the Bubble Sort algorithm.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example program to use the Bubble Sort function
if __name__ == "__main__":
    print("Welcome to the Bubble Sort Program!")
    
    # Input: Take a list of numbers from the user
    try:
        user_input = input("Enter numbers separated by spaces: ")
        arr = list(map(int, user_input.split()))
        
        # Output: Display the sorted list
        print("Original list:", arr)
        sorted_arr = bubble_sort(arr)
        print("Sorted list:", sorted_arr)
    except ValueError:
        print("Invalid input. Please enter only numbers separated by spaces.")
