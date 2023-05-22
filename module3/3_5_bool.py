# магические методы
# метод __bool__


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('call __len__')
        return abs(self.x - self.y)

    def __bool__(self):
        print('call __bool__')
        return self.x != 0 or self.y != 0

p1 = Point(1, 5)
# print(bool(p1))
p2 = Point(0, 0)
# print(bool(p2))


# task1
class City:
    def __init__(self, name):
        name = name.title()
        self.name = name

    def __str__(self):
        return self.name

    def __bool__(self):
        if self.name[-1] in ['a', 'e', 'i', 'o', 'u']:
            return False
        else:
            return True

p1 = City('new york')
assert p1.name == "New York"
assert p1.__str__() == "New York"
assert isinstance(p1, City)
print(p1)
assert bool(p1)


# task2
class Quadrilateral:
    def __init__(self, width, height=None):
        self.width = width
        self.height = (width if height is None else height)

    def __str__(self):
        if self.width == self.height:
            return f'Квадрат размером {self.width}х{self.height}'
        else:
            return f'Прямоугольник размером {self.width}х{self.height}'

    def __bool__(self):
        if self.width == self.height:
            return True
        else:
            return False


q1 = Quadrilateral(10)
print(q1)
assert q1.height == 10
assert q1.width == 10
assert bool(q1) is True
assert q1.__str__() == "Квадрат размером 10х10"
assert isinstance(q1, Quadrilateral)

q2 = Quadrilateral(3, 5)
print(q2)
assert q2.__str__() == "Прямоугольник размером 3х5"
assert bool(q2) is not True
assert isinstance(q2, Quadrilateral)

q3 = Quadrilateral(4, 7)
print(q3)
assert bool(q3) is False
assert q3.__str__() == "Прямоугольник размером 4х7"
assert isinstance(q3, Quadrilateral)

