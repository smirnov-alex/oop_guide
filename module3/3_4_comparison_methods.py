# Магические методы. Операции сравнения
# __eq__ - отвечает за ==
# __ne__ - Отвечает за !=
# __lt__ - Отвечает за <
# __le__ - Отвечает за <=
# __gt__ - Отвечает за >
# __ge__ - Отвечает за >=
from functools import total_ordering


class Rectangle:

    def __init__(self, a,b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            print('equal call')
            return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        print('less than call')
        if isinstance(other, Rectangle):
            return self.area < other.area
        elif isinstance(other, (int, float)):
            return self.area < other

    def __le__(self, other):
        print('less or equal call')
        return self == other or self < other


# Методы __eq__ и __hash__
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


p1 = Point(1, 2)
p2 = Point(1, 2)
# print(p1.__repr__())
# print(p1 == p2)
# print(p2.__hash__())

# hash есть у неизменяемых объектов (строка, кортеж, число). Те объекты, у которых есть хэш,
# могут использоваться в качестве ключей словаря

# если определен метод __eq__, то теряется возможность нахождения __hash__. Необходимо переопределить __hash__


@total_ordering
class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Fruit):
            return self.price == other.price
        elif isinstance(other, (int, float)):
            return self.price == other

    def __gt__(self, other):
        if isinstance(other, Fruit):
            return self.price > other.price
        elif isinstance(other, (int, float)):
            return self.price > other

    def __ge__(self, other):
        return self == other or self > other


class ChessPlayer:
    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, ChessPlayer):
            if self.rating == other.rating:
                return True
            else:
                return False
        elif isinstance(other, int):
            if self.rating == other:
                return True
            else:
                return False
        else:
            return 'Невозможно выполнить сравнение'

    def __gt__(self, other):
        if isinstance(other, ChessPlayer):
            if self.rating > other.rating:
                return True
            else:
                return False
        elif isinstance(other, int):
            if self.rating > other:
                return True
            else:
                return False
        else:
            return 'Невозможно выполнить сравнение'

    def __lt__(self, other):
        if isinstance(other, ChessPlayer):
            if self.rating < other.rating:
                return True
            else:
                return False
        elif isinstance(other, int):
            if self.rating < other:
                return True
            else:
                return False
        else:
            return 'Невозможно выполнить сравнение'

magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
assert magnus.name == 'Carlsen'
assert magnus.surname == 'Magnus'
assert magnus.rating == 2847
ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
assert not magnus == 4000
assert ian == 2789
assert not magnus == ian
assert magnus > ian
assert not magnus < ian
assert (magnus < [1, 2]) == 'Невозможно выполнить сравнение'
#print('Good')


@total_ordering
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area == other.area
        elif isinstance(other, (int, float)):
            return self.area == other

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area < other.area
        elif isinstance(other, (int, float)):
            return self.area < other



r1 = Rectangle(3, 4)
assert r1.width == 3
assert r1.height == 4
assert r1.area == 12
assert isinstance(type(r1).area, property), 'Вы не создали property area'

assert r1 > 11
assert not r1 > 12
assert r1 >= 12
assert r1 <= 12
assert not r1 > 13
assert not r1 == 13
assert r1 != 13
assert r1 == 12

r2 = Rectangle(2, 6)
assert r1 == r2
assert not r1 != r2
assert not r1 > r2
assert not r1 < r2
assert r1 >= r2
assert r1 <= r2

r3 = Rectangle(5, 2)
assert not r2 == r3
assert r2 != r3
assert r2 > r3
assert not r2 < r3
assert r2 >= r3
assert not r2 <= r3
print('Good')

