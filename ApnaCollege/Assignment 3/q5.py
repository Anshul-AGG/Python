# dictionary

student_marks = {}


def add_student():
    name = input("enter the name: ")
    if name in student_marks:
        print(f"{name} already added.")
    else:
        try:
            marks = int(input("Enter marks: "))
            student_marks[name] = marks
            print(f"{name} added successfully.")
        except ValueError:
            print("Marks must be an integer.")


def update_marks():
    name = input("Enter student name to update: ")
    if name in student_marks:
        try:
            new_marks = int(input("Enter new marks: "))
            student_marks[name] = new_marks
            print(f"{name}'s marks updated.")
        except ValueError:
            print("Marks must be an integer.")


def search_student():
    name = input("Enter student name to search: ")
    if name in student_marks:
        print(f"{name} has {student_marks[name]} marks.")
    else:
        print(f"{name} not found.")


def display_all():
    if student_marks:
        print("\nAll Students and Marks:")
        for name, marks in student_marks.items():
            print(f"{name}: {marks}")
    else:
        print("No student records found.")


while True:
    print("\nMenu:")
    print("A - Add a student")
    print("B - Update marks")
    print("C - Search for a student")
    print("D - Display all students and marks")
    print("E - Exit")

    choice = input("Enter your choice from A to D: ").upper()

    if choice == "A":
        add_student()
    elif choice == "B":
        update_marks()
    elif choice == "C":
        search_student()
    elif choice == "D":
        display_all()
    elif choice == "E":
        print("exiting program.")
        break
    else:
        print("Invalid choice, enter again.")
