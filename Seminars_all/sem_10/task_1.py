"""
Задание №1
Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.
"""

from math import pi


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    @staticmethod
    def length_circle(self) -> float:
        return 2 * pi * self.radius

    @staticmethod
    def square_circle(self) -> float:
        return pi * (self.radius ** 2)


temp = Circle(1)
print(Circle.length_circle(temp))
print(Circle.square_circle(temp))
