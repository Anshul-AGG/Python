# waf to write the factorial of n


def factorial(n):
    count = 1
    for i in range(1, n + 1):
        count *= i

    print("Factorial of", n, "is :", count)


factorial(5)


# waf to conver USD to INR


def convertor(n):
    if n != 0:
        print(n, "USD =", n * 88.57, "INR")
    else:
        print("Enter a positive number.")

    return n


convertor(100)


def conv(usd):
    inr = usd * 88
    print(usd, "USD =", inr, "INR")


conv(2)


# waf to say if a nummber is even or odd

def evenOdd(n):
    if n % 2 == 0:
        print(n ," is Even number")
    else:
        print(n, " is Odd")

evenOdd(3)