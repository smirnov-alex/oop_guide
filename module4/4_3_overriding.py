# переопределение методов


class Person:  # parent class

    def __init__(self, name):
        # print('init in class Person')
        self.name = name

    def walk(self):
        print('Человек идет')

    def breathe(self):
        print('Человек дышит')

    def sleep(self):
        print('Человек спит')

    def combo(self):
        self.breathe()
        self.walk()
        self.sleep()

    def __str__(self):
        return f'Person {self.name}'


class Doctor(Person):  # subclass

    def breathe(self):
        print('Доктор дышит')

    def __str__(self):
        return f'Doctor {self.name}'

# d = Doctor('Ivan')
# p = Person('Adam')
# d.breathe()
# p.breathe()
# p.walk()
# d.walk()
# print(p.name, d.name)
# print(p)
# print(d)
# p.combo()
# d.combo()

class Square:
    def get_value(self, a):
        return a * a


class Cube(Square):
    def get_value(self, a):
        return a ** 3

class Power4(Square):
    def get_value(self, a):
        return a ** 4

assert issubclass(Cube, Square)
assert issubclass(Power4, Square)

cube = Cube()

assert cube.get_value(2) == 8
assert cube.get_value(-17) == -4913

power4 = Power4()
assert power4.get_value(5) == 625
assert power4.get_value(25) == 390625

print('Good')

class CURD:
    def __init__(self):
        C().create()
        R().read()
        U().update()
        D().delete()


class C:
    def create(self):
        print("c", end='')


class U:
    def update(self):
        print("u", end='')


class R(C):
    def create(self):
        print("C", end='')

    def read(self):
        print("R", end='')


class D(U):
    def update(self):
        print("U", end='')

    def delete(self):
        print("D", end='')


CURD()

class MethodOverriding:
    def __init__(self):
        x = X()
        y = Y()
        y.method_2()
        x.method_1()
        y.method_1()
        x = y
        x.method_1() # № 1
        x.method_2() # № 2


class X:
    def method_1(self):
        print("m1 ~ X")


class Y(X):
    def method_1(self):
        print("m1 ~ Y")

    def method_2(self):
        print("m2 ~ Y")


MethodOverriding()
