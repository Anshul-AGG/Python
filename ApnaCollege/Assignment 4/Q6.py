# Abstraction

from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass


class Intern(Employee):
    def __init__(self, name, stipend):
        super().__init__(name)
        self.stipend = stipend

    def calculate_salary(self):
        return f"{self.name}'s salary as Intern is {self.stipend}"


class FullTimeEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def calculate_salary(self):
        return f"{self.name} salary is {self.salary}"


class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        total = self.hourly_rate * self.hours_worked
        return f"{total} salary as COntract employee"


employees = [
    Intern("Ansh", 10000),
    FullTimeEmployee("AnShu", 20000),
    ContractEmployee("AHJHI", 120, 20),
]

for emp in employees:
    print(emp.calculate_salary())
