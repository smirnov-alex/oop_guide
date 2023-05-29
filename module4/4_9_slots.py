# Slots. Ограничение атрибутов для класса
# занимает меньше памяти (из-за отсутствия __dict__)
# операции над объектом выполняются быстрее
from timeit import timeit


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

# p1 = Point(2, 3)
# print(p1.x)
# print(p1.__dict__)
# p1.q = 100
# print(p1.q)


class PointSlots:

    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

p2 = PointSlots(2, 3)
print(p2.x)
# print(p2.__dict__)  # ошибка
# p2.q = 100  # ошибка AttributeError


def make_cl1():
    s = Point(5, 90)
    s.x = 100
    s.x
    del s.x


def make_cl2():
    d = PointSlots(5, 90)
    d.x = 999
    d.x
    del d.x

print(timeit(make_cl1))
print(timeit(make_cl2))
# print(s.__sizeof__(), s.__dict__.__sizeof__())
# print(d.__sizeof__())


class Phone:
    __slots__ = ['brand', 'model', '__dict__']


phone1 = Phone()
phone1.brand = 'Apple'
phone1.model = 'iPhone 14'

print(phone1.brand)
print(phone1.model)
phone1.price = 1000
print(phone1.price)


class Person:
    __slots__ = ('first_name', 'last_name', 'age')

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old"

arshavin = Person("Andrew", "Arshavin", 35)
assert arshavin.first_name == 'Andrew'
assert arshavin.last_name == 'Arshavin'
assert arshavin.age == 35
print(arshavin)

mg = Person("Max", "Galkin", 44)
assert mg.first_name == 'Max'
assert mg.last_name == 'Galkin'
assert mg.age == 44
print(mg)

try:
    arshavin.city = 'SPB'
except AttributeError:
    print('Нельзя создавать новые атрибуты')
