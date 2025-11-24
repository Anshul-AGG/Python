# merge lists

l1 = list(map(int, input("Enter numbers: ").split()))
l2 = list(map(int, input("Enter numbers: ").split()))

result = l1 + l2
result.sort()
print(result)
