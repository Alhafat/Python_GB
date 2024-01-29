"""
На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
Первый список ваш лотерейный билет.
Второй список содержит список чисел, которые выпали в лотерею.
Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.

Напишите класс LotteryGame, который будет иметь метод compare_lists, который будет сравнивать числа из вашего билета из
list1 со списком выпавших чисел list2

Если совпадающих чисел нет, то выведите на экран:
Совпадающих чисел нет.

Пример входных данных:


list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()
Пример выходных данных:


Совпадающие числа: [3, 12, 8, 41, 9, 14, 5]
Количество совпадающих чисел: 7
"""


class LotteryGame:
    def __init__(self, lst_1, lst_2):
        self.list_1 = lst_1
        self.list_2 = lst_2

    @staticmethod
    def compare_lists():
        list_result = []
        for i in range(len(list_1)):
            if list_1[i] in list_2:
                list_result.append(list_1[i])
        if len(list_result) != 0:
            print(f"Совпадающие числа: {list_result}\nКоличество совпадающих чисел: {len(list_result)}")
        else:
            print(f"Совпадающих чисел нет.")
        return list_result


list_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

game = LotteryGame(list_1, list_2)
matching_numbers = game.compare_lists()
