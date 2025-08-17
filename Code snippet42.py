def word_frequency(sentence):
    freq = {}
    words = sentence.split()
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

# Example
print(word_frequency("python is great and python is easy"))
# Output: {'python': 2, 'is': 2, 'great': 1, 'and': 1, 'easy': 1}
