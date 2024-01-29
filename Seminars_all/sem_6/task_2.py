"""
Создайте модуль с функцией внутри.
� Функция принимает на вход три целых числа: нижнюю и
верхнюю границу и количество попыток.
� Внутри генерируется случайное число в указанных границах
и пользователь должен угадать его за заданное число
попыток.
� Функция выводит подсказки “больше” и “меньше”.
� Если число угадано, возвращается истина, а если попытки
исчерпаны - ложь
"""

import random


def main(min=1, max=10, count=3):
    num = random.randint(min, max)
    # print(num)
    temp = 0
    while count > temp:
        number = int(input("enter you number?: "))
        if number == num:
            print(f"you win! its {number == num}")
            break
        elif number > num:
            print("Почти верно, нужно поменьше, попробуй еще раз!")
            temp += 1
            continue
        elif number < num:
            print("Почти верно, нужно побольше, попробуй еще раз!")
            temp += 1
            continue
    else:
        if input("You loose, can u try again? --> Y/n: \n").lower() == "y":
            main()
        else:
            print("good by!")

if __name__ == '__main__':
    print("hello user! ")
    main()

