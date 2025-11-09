class student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avgMarks(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(self.name, " Your avg score is", sum / 3)


s1 = student("Anshul", [99, 98, 54])
s1.avgMarks()
