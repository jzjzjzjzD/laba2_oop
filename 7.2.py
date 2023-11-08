class Employee:
    name = None
    salary = None
    def show(self):
        print(self.salary)
employee = Employee()
employee.name = "Danya"
employee.salary = 5000
employee.show()