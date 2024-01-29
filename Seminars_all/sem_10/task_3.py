"""
Задание №3
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
"""


class Person(object):
    def __init__(self, name, __birthday, full_name):
        self.name = name
        self.__birthday = __birthday
        self.full_name = full_name

    @staticmethod
    def birthday(self):
        self.__birthday += 1
        return self.__birthday

    @staticmethod
    def full_name(self):
        return self.full_name

    @staticmethod
    def get_birthday(self):
        return f'Corrent birthday {self.__birthday}'


person = Person('John', 1989, '<NAME>')
print(Person.full_name(person))
print(Person.get_birthday(person))
print(Person.birthday(person))
