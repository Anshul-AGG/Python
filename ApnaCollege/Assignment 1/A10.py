"""Take a decimal number as input (like 45.78) and output its:
•integer part - 45
•fractional part - .78"""

n = float(input("Enter the number: "))
n1 = int(n)


float_int = n - n1

print(n1)
print(f"fractional part is {float_int: .2f}")
