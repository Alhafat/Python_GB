"""
Создайте файл, в котором вы импортируете встроенные в
модуль функции под псевдонимами. (3-7 строк импорта)
"""


from math import sqrt as s
from math import pow as p

a = 4
q = 2
res = s(a)
print(res)
res = p(q, 2)
print(res)