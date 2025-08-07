def find_duplicates(lst):
    seen = []
    duplicates = []
    for item in lst:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        else:
            seen.append(item)
    return duplicates

# Example
print(find_duplicates([1, 2, 3, 4, 2, 5, 3]))  # [2, 3]
