def most_frequent_char(text):
    text = text.replace(" ", "").lower()
    freq = {}

    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1

    most_freq = max(freq, key=freq.get)
    print("Most frequent character:", most_freq)
    print("Frequency:", freq[most_freq])

# Example usage
input_str = input("Enter a string: ")
most_frequent_char(input_str)
