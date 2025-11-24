# palindrome or not

string = input("enter string: ")
rev_string = ""
for i in string:
    rev_string = i + rev_string

if rev_string == string:
    print("Palindrome")
else:
    print("Not palindrome")
