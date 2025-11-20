#sum og digits of a number, n

def Digits_sum():
    n = int(input("Enter the number: "))
    total = 0
    while n > 0:
        digits = n % 10
        total += digits
        n = n // 10
    print(total)        

Digits_sum()