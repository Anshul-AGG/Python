# Program to find duplicate elements in a list

my_list = [1, 2, 3, 2, 4, 5, 3, 6, 1]
seen = set()
duplicates = set()

for item in my_list:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

print("Elements that appear more than once:", list(duplicates))