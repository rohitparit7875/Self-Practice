def to_lowercase(char):
    # Convert uppercase letter to lowercase manually
    if 'A' <= char <= 'Z':
        return chr(ord(char) + 32)
    return char

def are_anagrams(s1, s2):
    # Step 1: Convert both strings to lowercase manually and remove spaces
    str1 = ''
    for ch in s1:
        if ch != ' ':
            str1 += to_lowercase(ch)

    str2 = ''
    for ch in s2:
        if ch != ' ':
            str2 += to_lowercase(ch)

    # Step 2: Count characters manually
    if len(str1) != len(str2):
        return False

    count = [0] * 256  # Assuming extended ASCII

    for i in range(len(str1)):
        count[ord(str1[i])] += 1

    for i in range(len(str2)):
        count[ord(str2[i])] -= 1

    for i in range(256):
        if count[i] != 0:
            return False

    return True

# Example usage
print(are_anagrams("Listen", "Silent"))  # True
print(are_anagrams("Hello", "World"))    # False
