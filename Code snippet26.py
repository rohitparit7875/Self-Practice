def reverse_string(s):
    result = ""
    for char in s:
        result = char + result
    return result

# Example
print(reverse_string("Python"))  # Output: nohtyP
