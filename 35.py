def count_words(sentence):
    i = 0
    word_count = 0
    in_word = False
    while i < len(sentence):
        if sentence[i] != ' ' and not in_word:
            in_word = True
            word_count += 1
        elif sentence[i] == ' ':
            in_word = False
        i += 1
    return word_count

# User input
sentence = input("Enter a sentence: ")
print("Number of words:", count_words(sentence))
