def second_largest(lst):
    unique_sorted = sorted(set(lst), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None

# Example Usage
numbers = [4, 1, 7, 4, 8, 7]
print("Second Largest:", second_largest(numbers))
