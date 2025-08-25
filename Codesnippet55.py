text = "hello world hello GitHub streak"
words = text.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Word Frequencies:", freq)
