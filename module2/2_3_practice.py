# Практика. Класс Point
from math import sqrt


class Point:

    list_points = []

    def __init__(self, coord_x=0, coord_y=0):
        self.move_to(coord_x, coord_y)
        Point.list_points.append(self)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0, 0)

    def print_point(self):
        print(f'Точка с координатами ({self.x}, {self.y})')

    def calc_distance(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError("Аргумент должен принадлежать классу Point")
        return sqrt((self.x - another_point.x)**2 + (self.y - another_point.y)**2)


p1 = Point(3, 4)
p2 = Point(-54, 32)
p3 = Point()
p7 = Point(6, 0)
p8 = Point(0, 8)
p2.print_point()
# p7.calc_distance(90)
print(p7.calc_distance(p8))
print(Point.list_points)
print(Point.list_points[1].x)

# моносостояние атрибутов класса
'''
Если вы хотите, чтобы у всех ваших экземпляров были одни общие атрибуты, вы можете воспользоваться паттерном 
«Моносостояние». Он позволяет реализовать одно состояние для атрибутов всех наших ЭК.
'''
class Cat:
    __shared_attr = {
        'breed': 'pers',
        'color': 'black',
    }
    def __init__(self):
        self.__dict__ = Cat.__shared_attr
