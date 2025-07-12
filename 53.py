# Code 2: Counting with dictionary
items = ['pen', 'book', 'pen', 'pencil', 'book', 'book']

count_dict = {}
for item in items:
    count_dict[item] = count_dict.get(item, 0) + 1

print("Item counts:", count_dict)
