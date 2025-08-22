def reverse_string(s):
    result = ""
    for char in s:
        result = char + result
    return result

# Test
s = "Qualys"
print("Reversed string:", reverse_string(s))
