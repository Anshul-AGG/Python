class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("Role = ", self.role)
        print("Department = ", self.department)
        print("Salary = ", self.salary)

e1 = ("SDE 1", "Developer", "1,00,000")
print(e1)   
class Engineer(Employee):
    def __init__(self, role, department, salary, name, age):
        super().__init__(role, department, salary)
        self.name = name
        self.age = age


        