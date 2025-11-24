# Program to check if two lists have no common elements

list1 = [1, 2, 3, 5]
list2 = [5, 6, 7, 8]

# Convert lists to sets and check intersection
if set(list1).isdisjoint(set(list2)):
    print("The lists share no common elements.")
else:
    print("The lists share common elements.")
