class Employee:
    name = None
    salary = None
    def show(self):
        print(self.name)
employee = Employee()
employee.name = "Danya"
employee.salary = 5000
employee.show()