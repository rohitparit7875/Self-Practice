text = "programming"
freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

print("Character Frequency:", freq)
