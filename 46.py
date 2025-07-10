def replace_vowels(text):
    vowels = 'aeiouAEIOU'
    result = ''
    for ch in text:
        if ch in vowels:
            result += chr(ord(ch) + 1)
        else:
            result += ch
    return result

# Example usage
input_text = input("Enter a string: ")
print("Output:", replace_vowels(input_text))
