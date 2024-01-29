"""
Задание №5
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.
"""


class Bird:
    def __init__(self, name, old, ability):
        self.name = name
        self.old = old
        self.ability = ability

    @staticmethod
    def get_ability(self):
        return self.ability


class Dog:
    def __init__(self, name, old, ability):
        self.name = name
        self.old = old
        self.ability = ability

    @staticmethod
    def get_ability(self):
        return self.ability


class Cat:
    def __init__(self, name, old, ability):
        self.name = name
        self.old = old
        self.ability = ability

    @staticmethod
    def get_ability(self):
        return self.ability


cat = Cat('cat', 15, 'meow')
dog = Dog('dog', 5, 'ow')
bird = Bird('bird', 1, 'chick')

print(cat.get_ability(cat))
print(dog.get_ability(dog))
print(bird.get_ability(bird))
