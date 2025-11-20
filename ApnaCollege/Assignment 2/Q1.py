"""Write a program that takes salary as input. Using conditional statements, calculate the final tax rate
based on these rules

• If salary < 30,000 → 5%
• If salary is 30,000-70,000 → 15%
• If salary > 70,000 → 25%
"""
salary = float(input("Enter your salary: "))


if salary < 30000:
    tax_rate = 0.05
if salary >= 30000 and salary <= 70000:
    tax_rate = 0.15
if salary > 70000:
    tax_rate = 0.25

print(f"Your tax rate is {tax_rate * 100}%.")
