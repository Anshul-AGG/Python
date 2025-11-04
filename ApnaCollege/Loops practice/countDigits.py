#Count the total number of digits in a number using while loop

num = 784223
count = 0

while num != 0:
    num = num // 10  # // is floor division operator
    count+=1
print(count)


