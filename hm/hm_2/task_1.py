"""
Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.

Пример

На входе:


num = 255
На выходе:


Шестнадцатеричное представление числа: FF
Проверка результата: 0xff
"""


def num_after_256(num, number):
    temp = int(str(num)[0:2])
    pass


def num_bit_depth(num, number):
    if num < 256:
        num_before_256(num, number)
    else:
        num_after_256(num, number)


def num_before_256(num, number):
    while num >= 16:
        num, number = add_letter(num, number)
    else:
        num, number = add_letter(num, number)
    print(number)


def add_letter(num, number):
    temp = num // 16
    if temp == 0:
        temp = num
        num = 0
    match temp:
        case 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9:
            number += str(temp)
        case 10:
            number += "a"
        case 11:
            number += "b"
        case 12:
            number += "c"
        case 13:
            number += "d"
        case 14:
            number += "e"
        case 15:
            number += "f"
        case _:
            number += str(temp)
    num -= temp * 16
    return num, number


def main():
    num = 255
    print(hex(num))
    number = "0x"
    num_bit_depth(num, number)


if __name__ == '__main__':
    main()
