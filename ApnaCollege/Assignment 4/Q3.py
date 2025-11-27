# Encapsualtion


class Student:

    def __init__(self, name, roll_no, marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks

        # self.set_name(name)
        # self.set_marks(marks)
        # self.set_roll_no(roll_no)

    def get_name(self):
        return self.__name

    def get_marks(self):
        return self.__marks

    def get_roll_no(self):
        return self.__roll_no

    def set_name(self, name):
        if isinstance(name, str) and name.strip():
            self.__name = name.strip()
        else:
            raise ValueError("Name can't be empty.")

    def set_marks(self, marks):
        if isinstance(marks, (int, float)) and marks >= 0:
            self.__marks = marks
        else:
            raise ValueError("Marks can't be negative.")

    def set_roll_no(self, roll_no):
        if isinstance(roll_no, int) and 1 <= roll_no <= 100:
            self.__roll_no = roll_no
        else:
            raise ValueError("Roll nuimber must be between 1 and 100.")


try:
    s1 = Student("Anshul", 42, 88.5)
    print("Name:", s1.get_name())
    print("Roll No:", s1.get_roll_no())
    print("Marks:", s1.get_marks())
except ValueError as e:
    print("Error:", e)
