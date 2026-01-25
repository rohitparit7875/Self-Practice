word = "automation"
count = 0

for ch in word:
    if ch in "aeiouAEIOU":
        count += 1

print("Number of vowels:", count)
