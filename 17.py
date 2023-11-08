class Employee:
    __name = None
    __surname = None

    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    def getName(self):
        return self.__name

    def getSurname(self):
        return self.__surname

    def setName(self, name):
        self.__name = name

    def setSurname(self, surname):
        self.__surname = surname

employee = Employee("Danil", "Berezin")
employee.setName("Danil")
employee.setSurname("Berezin")
print(employee.getName())
print(employee.getSurname())
