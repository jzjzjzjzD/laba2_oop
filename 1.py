class Car:
    def __init__(self):
        self.color = ''
        self.fuel = 0
        self.brand = ''
        self.year = 0

    def go(self):
        print("Автомобиль поехал.")

    def turn(self):
        print("Автомобиль повернул.")

    def stop(self):
        print("Автомобиль остановился.")

    def info(self):
        print("Информация об автомобиле:")
        print(f"Марка: {self.brand}")
        print(f"Год выпуска: {self.year}")
        print(f"Цвет: {self.color}")
        print(f"Уровень топлива: {self.fuel}")

myCar = Car()

myCar.color = 'black'
myCar.fuel = 52
myCar.brand = 'bmw'
myCar.year = 2023

myCar.info()