#marks from 3 subjects from user and store them in dictionary 
# start with empty dict and add 1 by 1.

marks = {}

subject1 = int(input("Enter the marks of physics : "))
marks.update({"physics" : subject1})

subject2 = int(input("Enter the marks of Maths: "))
marks.update({"Maths" : subject2})

subject3 = int(input("Enter the marks of Chemistry: "))
marks.update({"Chemistry" : subject3})


print(marks)