# print even number between two numbers

n = int(input("Enter 1st number: "))
n1 = int(input('Enter 2nd number: '))

for i in range(n, n1+1):
    if i % 2 == 0:
        print(i)

else:
    print("Not found")