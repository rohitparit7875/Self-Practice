def has_duplicates(elements):
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            if elements[i] == elements[j]:
                print("List has duplicates.")
                return
    print("List has all unique elements.")

# Input from user
user_input = input("Enter list elements separated by space: ")
elements = []
word = ""
for ch in user_input:
    if ch == " ":
        elements.append(word)
        word = ""
    else:
        word += ch
if word:
    elements.append(word)

has_duplicates(elements)
