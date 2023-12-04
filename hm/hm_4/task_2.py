"""
Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ - значение переданного аргумента, а значение - имя аргумента.
Если ключ не хешируем, используйте его строковое представление.

params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)
На выходе:


{1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}
f'{b=}'.split('=')[0].split('.')[-1])
"""


def key_params(**kwargs):
    dict_temp = {}
    for key, value in kwargs.items():
        dict_temp.update(
            {value if type(value) is int or type(value) is bool or type(value) is float else f'{value}': key})
    return dict_temp


def main():
    params = key_params(a=3.14, b='hello', c=[1, 2, 3], d={})
    print(params)


if __name__ == '__main__':
    main()
