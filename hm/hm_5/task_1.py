"""
Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

Пример использования.
На входе:


file_path = "C:/Users/User/Documents/example.txt"

На выходе:


('C:/Users/User/Documents/', 'example', '.txt')
"""


def get_file_info(file_path):
    temp = file_path.split(".")
    temp_1 = file_path.split("/")
    # print(temp)
    # print(temp_1)
    tem_2 = temp_1[-1].split(".")
    # print(tem_2)
    a,b,c = (f'{"/".join(temp_1[:-1])+"/"}', f'{tem_2[0]}', f'.{tem_2[-1]}')
    return a,b,c

global file_path
file_path = "C:/Users/User/Documents/example.txt"
print(get_file_info(file_path))
