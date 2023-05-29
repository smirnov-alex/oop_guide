# inheritance
# Наследование. Введение


class Person:  # parent class
    def can_walk(self):
        print('Я могу ходить')

    def can_breath(self):
        print('Я могу дышать')


class Doctor(Person):  # subclass

    def can_cure(self):
        print('Я могу лечить')


class Ortoped(Doctor):
    pass


class Architect(Person):  # subclass

    def can_build(self):
        print('Я могу построить здание')

d = Doctor()
d.can_cure()
d.can_walk()
a = Architect()
a.can_build()
a.can_breath()
print(issubclass(Doctor, Person))  # проверить
print(isinstance(d, Doctor))
print(isinstance(d, Person))

o = Ortoped()
print(isinstance(o, Person))
o.can_breath()


# task2
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def display_info(self):
        print(f'Vehicle Name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}')


class Bus(Vehicle):
    pass

bus_99 = Bus("Ikarus", 66, 124567)
bus_99.display_info()  # печатает "Vehicle Name: Ikarus, Speed: 66, Mileage: 124567"


# task3
class Person:  # parent class
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    @staticmethod
    def is_employee():
        return False


class Employee(Person):
    @staticmethod
    def is_employee():
        return True


emp1 = Person("vasya")
print(emp1.get_name(), emp1.is_employee())  # vasya False

emp2 = Employee("gena bukin")
print(emp2.get_name(), emp2.is_employee())  # gena bukin True
