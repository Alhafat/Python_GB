"""
Задание №2
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
"""


class Rectangle:
    def __init__(self, a: float = None, b: float = None):
        # if self.a is None:
        #     self.a = self.b
        # elif self.b is None:
        #     self.b = self.a
        # else:
        self.a = a
        self.b = b

    @staticmethod
    def length_rectangle(self) -> float:
        if self.a is None:
            self.a = self.b
        elif self.b is None:
            self.b = self.a
        else:
            return 2 * (self.a + self.b)
        return 2 * (self.a + self.b)

    @staticmethod
    def square_rectangle(self) -> float:
        if self.a is None:
            self.a = self.b
        elif self.b is None:
            self.b = self.a
        else:
            return self.a * self.b
        return self.a * self.b


temp = Rectangle(20)
print(Rectangle.length_rectangle(temp))
print(Rectangle.square_rectangle(temp))
