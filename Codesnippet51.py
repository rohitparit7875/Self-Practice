def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# Test
s = "qualys"
print("Character frequency:", char_frequency(s))
