# inheritance
# Наследование. Введение, часть 2
# любой класс по умолчанию наследуется от object


class Person:
    pass


class Mylist(list):
    pass


class Doctor(Person):
    pass


class Architect(Person):
    pass


# print(isinstance(34, object))
# print(isinstance(dict, object))
# print(issubclass(int, object))
# print(issubclass(Person, object))
# print(dir(object))
#
# t = Mylist()
# print(t)
# t.append('hello')
# print(t)
# print(type(t))  # <class '__main__.Mylist'>

# task
class NewInt(int):
    def __init__(self, x):
        self.x = x

    def repeat(self, n=2):
        return str(self.x) * n

    def to_bin(self):
        return int(f'{self.x:b}')

a = NewInt(9)
print(a.repeat())  # печатает число 99
d = NewInt(a + 5)
print(d.repeat(3)) # печатает число 141414
d = NewInt(a + 5)
b = NewInt(NewInt(7) * NewInt(5))
print(b)
print(b.to_bin()) # печатает 100011 - двоичное представление числа 35