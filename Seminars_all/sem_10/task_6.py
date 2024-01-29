"""
Задание №6
Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс
Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.
"""
from args import args


class Animal:
    def __init__(self, name, old, ability):
        self.name = name
        self.old = old
        self.ability = ability

    @staticmethod
    def get_ability(self):
        return self.ability


class Bird(Animal):
    def __init__(self, tupe, *args):
        super().__init__(*args)
        self.type = tupe


class Dog(Animal):
    def __init__(self, tupe, *args):
        self.type = tupe
        super().__init__(*args)


class Cat(Animal):
    def __init__(self, tupe, *args):
        self.type = tupe
        super().__init__(*args)


a_1 = Cat('cat', 'name_1', 15, 'meow')
dog = Dog('dog', 'name_2', 10, 'ow')
bird = Bird('bird', 'name_3', 1, 'chick')

print(Cat.get_ability(a_1))
print(dog.get_ability(dog))
print(bird.get_ability(bird))
