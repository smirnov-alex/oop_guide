'''
class Robot:
    def set_name(self, name):
        self.name = name

    def say_hello(self):
        if hasattr(self, 'name'):
            print(f'Hello, human! My name is {self.name}')
        else:
            print('У робота нет имени')

    def say_bye(self):
        print('See u later alligator')


c3po = Robot()
r2d2 = Robot()
c3po.say_hello()
c3po.say_bye()
r2d2.say_hello()
r2d2.say_bye()



class Counter:
    def start_from(self, num=0):
        self.start = num

    def increment(self):
        self.start += 1

    def display(self):
        print(f'Текущее значение счетчика = {self.start}')

    def reset(self):
        self.start = 0

class Constructor():
    def add_atribute(self, name, value):
        setattr(self, name, value)

    def display(self):
        self.__dict__
'''


class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, instance):
        if isinstance(instance, Point):
            d = ((self.x - instance.x)**2 + (self.y - instance.y)**2)**0.5
            return d
        else:
            print('Передана не точка')

p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
p3 = Point()
p3.set_coordinates(10, 10)
p1.set_coordinates(4, 2)
print(p1.get_distance(p3))
