# waf to print the elements of a list in a single line

l1 = [1, 23, 56, 6]
l2 = [1.4, 55, 223, 0]


def single_line(list):
    for item in list:
        print(item, end=" ")


single_line(l1)
single_line(l2)
