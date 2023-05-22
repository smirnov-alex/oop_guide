# Магические методы. __len__ и __abs__
# __len__ - найти длину объекта
# __abs__ - найти модуль числа

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __len__(self):
        return len(self.name + self.surname)

a = Person('ivan', 'ivanov')
# print(len(a))


class Otrezok:
    def __init__(self, point1, point2):
        self.x1 = point1
        self.x2 = point2

    def __len__(self):
        return abs(self)

    def __abs__(self):
        return abs(self.x2 - self.x1)

t = Otrezok(5, 9)
f = Otrezok(15, 9)

# print(len(t))
# print(len(f))


class Hero:
    def __len__(self):
        return len(self.__dict__)

    def __str__(self):
        if self.__len__() == 0:
            return ''
        else:
            answer: str = ''
            for key, value in sorted(self.__dict__.items(), key=lambda para: para[0]):
                answer += f'{key}: {str(value)}\n'
            return answer.rstrip('\n')

hero = Hero()
assert len(hero) == 0
hero.health = 50
hero.damage = 10
assert len(hero) == 2
assert str(hero) == '''damage: 10
health: 50'''
hero.weapon = ['sword', ' bow']
hero.skill = 'Некромант'
assert str(hero) == '''damage: 10
health: 50
skill: Некромант
weapon: ['sword', ' bow']'''
print(hero)