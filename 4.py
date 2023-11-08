class Employee:
    def __init__(self):
        self.name = None
        self.salary = None
        self.name1 = None
        self.salary1 = None

employee = Employee()

employee.name = 'Danil'
employee.salary = "50000"
employee.name1 = 'Daniil'
employee.salary1 ="10000"

print(f"Имя: {employee.name}")
print(f"Зарплата: {employee.salary}")
print(f"Имя: {employee.name1}")
print(f"Зарплата: {employee.salary1}")