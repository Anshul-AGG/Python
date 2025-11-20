# prints digits of a number

n = int(input("enter the number: "))


while n > 0:
    print(n % 10)
    n = n // 10

