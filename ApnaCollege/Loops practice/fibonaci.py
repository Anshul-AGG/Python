#Display Fibonacci series up to 10 terms

n1 = 0
n2 = 1

for i in range(10):
    print(n1, end=" ")
    res = n1 + n2

    n1 = n2
    n2 = res


n1 , n2 = 0, 1 
count = 1

while True:
    f1 = n1+n2
    count += 1
    print(n1, end=" ")
    if count == 10:
        break
    n1 = n2 
    n2 = f1
