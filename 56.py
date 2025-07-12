sentence = input("Enter a sentence: ")
words = sentence.split()
long_words = [word for word in words if len(word) > 5]

print("Words with more than 5 letters:", long_words)
