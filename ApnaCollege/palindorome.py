# check if list has palindrome

#l1 = [1, 2, 3, 2 , 1]
l1 = [1, "abc", "abc", 1]

l2 = l1.copy()

l2.reverse()

print(l2)

if l2 == l1:
    print("Palindrome")
else:
    print("Nope")