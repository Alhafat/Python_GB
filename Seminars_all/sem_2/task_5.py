"""
Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
Используйте комплексные числа для извлечения квадратного корня.
"""
import math

a, b, c = int(input("a: ")), int(input("b: ")), int(input("c: "))
d = math.pow(b, 2) - 4 * a * c
if d > 0:
    print((-1 * b - math.sqrt(d)) / (2 * a))
    print((-1 * b + math.sqrt(d)) / (2 * a))
elif d == 0:
    print(-1 * (b / (2 * a)))
else:
    d = complex(d, 0)
    print(f"complex sqrt{(-1 * b - d ** 0.5) / (2 * a)}")
    print(f"complex sqrt{(-1 * b + d ** 0.5) / (2 * a)}")
