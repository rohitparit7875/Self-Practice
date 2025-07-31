from collections import Counter

sentence = "this is a test this is only a test"
words = sentence.split()
frequency = Counter(words)

print(frequency)
# Output: Counter({'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1})
