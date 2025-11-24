numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

even_num = tuple(num for num in numbers if num % 2 == 0)

odd_num = tuple(num for num in numbers if num % 2 != 0)

print(even_num)
print(odd_num)
