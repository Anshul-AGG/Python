# print number of spaces in string

word = input("Enter any strings: ")

# count = word.count(" ")
# print(count)

count = 0
for ch in word:
    if ch == " ":
        count += 1
print(count)
