def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase for accurate comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if sorted characters of both strings are equal
    return sorted(str1) == sorted(str2)

# Example usage
input1 = input("Enter the first string: ")
input2 = input("Enter the second string: ")

if is_anagram(input1, input2):
    print(f"'{input1}' and '{input2}' are anagrams!")
else:
    print(f"'{input1}' and '{input2}' are not anagrams.")
