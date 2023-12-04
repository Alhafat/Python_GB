"""
Задание №3

✔ Создайте вручную кортеж содержащий элементы разных типов.

✔ Получите из него словарь списков, где:

ключ — тип элемента,

значение — список элементов данного тип
"""

# temp = tuple((123, 1235, "sfds", "aa", True, "adjl", False))
# print(temp)
# dict_temp = dict()
# for i in temp:
#     if dict_temp.get(type(i)) is not None:
#         for key, value in dict_temp.items():
#             dict_temp[key].append(i)
#             continue
#     dict_temp.update({type(i): [i]})
#
# print(dict_temp)

"""
Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь, 
где ключ - значение переданного аргумента, а значение - имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
"""


def key_params(b, temp):
    dict_temp = {}
    dict_temp.update({b: temp})
    return dict_temp


def main():
    b = 1
    print(key_params(b, f'{b=}'.split('=')[0].split('.')[-1]))


if __name__ == '__main__':
    main()
