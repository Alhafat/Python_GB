"""
Задание №4
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь
"""
from Seminars_all.sem_10.task_3 import person


class Worker:
    def __init__(self, id):
        self.id = id

    def unlock(self):
        list_1 = [int(i) for i in str(self.id)]
        temp = sum(list_1) % len(list_1)
        return f'уровень доступа - {temp}'



person.Person = Worker(1234567891011121)
print(Worker.unlock(person.Person))
