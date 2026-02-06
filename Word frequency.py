sentence = input("Enter a sentence: ")
words = sentence.split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

for key, value in freq.items():
    print(key, ":", value)
