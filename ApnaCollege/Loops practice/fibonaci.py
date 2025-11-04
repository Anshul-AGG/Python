#Display Fibonacci series up to 10 terms

n1 = 0
n2 = 1

for i in range(10):
    print(n1, end=" ")
    res = n1 + n2

    n1 = n2
    n2 = res