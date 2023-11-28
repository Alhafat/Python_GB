"""
Задание №4
✔ Напишите программу, которая вычисляет площадь
круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять
не менее 42 знаков после запятой.
"""
import decimal
import math


# print(decimal(math.pi * 500 ** 2, 42))

decimal.getcontext().prec = 42
diameter = decimal.Decimal(input("Введите диаметр: "))
PI = decimal.Decimal(math.pi)
print("Длина окружности равна", PI * diameter)
print("Площадь окружности равна", PI * (diameter / 2) ** 2)
