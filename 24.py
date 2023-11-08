class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

employees = [
Employee("Колян", 502000),
Employee("Ваня", 111111),
Employee("Петя", 40000)
]

for employee in employees:
    print(employee.get_name())
    print(employee.get_salary())
    print()