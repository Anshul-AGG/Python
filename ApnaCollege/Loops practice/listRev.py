list1 = [1, 2, 3, 4, 5, 6, 7, 8]

# size = len(list1) - 1

# for i in range(size, -1, -1):
#     print(list1[i])

new_list = reversed(list1)
for i in new_list:
    print(i)