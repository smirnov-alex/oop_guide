# Делегирование
# в дочернем классе вызывается метод родительского класса через super()

class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Person {self.name} {self.surname}'

    def info(self):
        print('Parent class')
        print(self)

    def breathe(self):
        print('Человек дышит')


class Doctor(Person):

    def __init__(self, name, surname, age):
        super().__init__(name, surname)
        self.age = age

    def __str__(self):
        return f'Doctor {self.name} {self.surname}'

    def breathe(self):
        super().breathe()
        print('Доктор дышит')


# p = Person('Tony', 'Stark')
# d = Doctor('Stephen', 'Strange', 38)
# d.breathe()
# print(p.name, p.surname)
# print(d.name, d.surname, d.age)
# d.info()


# task1
class Person:

    def __init__(self, name, passport):
        self.name = name
        self.passport = passport

    def display(self):
        print(f'{self.name}: {self.passport}')


class Employee(Person):

    def __init__(self, name, passport, salary, department):
        super().__init__(name, passport)
        self.salary = salary
        self.department = department


# task2
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

    def display(self):
        print(f'Total {self.name} fare is: {self.fare()}')


class Bus(Vehicle):
    def __init__(self, name, mileage, capacity=50):
        super().__init__(name, mileage, capacity)

    def fare(self):
        return super().fare() * 1.1


class Taxi(Vehicle):
    def __init__(self, name, mileage, capacity=4):
        super().__init__(name, mileage, capacity)

    def fare(self):
        return super().fare() * 1.35

# sc = Vehicle('Scooter', 100, 2)
# sc.display()
#
# merc = Bus("Mercedes", 120000)
# merc.display()
#
# polo = Taxi("Volkswagen Polo", 15000)
# polo.display()


# task3
class Transport:
    def __init__(self, brand, max_speed, kind=None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self):
        return f'Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч'


class Car(Transport):
    def __init__(self, brand, max_speed, mileage, gasoline_residue):
        super().__init__(brand, max_speed, kind='Car')
        self.mileage = mileage
        self.__gasoline_residue = gasoline_residue

    @property
    def gasoline(self):
        return f'Осталось бензина {self.__gasoline_residue} л'

    @gasoline.setter
    def gasoline(self, value):
        if not isinstance(value, int):
            print('Ошибка заправки автомобиля')
        else:
            self.__gasoline_residue += value
            print(f'Объем топлива увеличен на {value} л и составляет {self.__gasoline_residue} л')


class Boat(Transport):
    def __init__(self, brand, max_speed, owners_name):
        super().__init__(brand, max_speed, kind='Boat')
        self.owners_name = owners_name

    def __str__(self):
        return f'Этой лодкой марки {self.brand} владеет {self.owners_name}'


class Plane(Transport):
    def __init__(self, brand, max_speed, capacity):
        super().__init__(brand, max_speed, kind='Plane')
        self.capacity = capacity

    def __str__(self):
        return f'Самолет марки {self.brand} вмещает в себя {self.capacity} людей'


# task4
class Initialization:
    def __init__(self, capacity: int, food: list):
        if isinstance(capacity, int):
            self.capacity = capacity
            self.food = food
        else:
            print('Количество людей должно быть целым числом')


class Vegetarian(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f"{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}"


class MeatEater(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f"{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}"


class SweetTooth(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f"Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}"

    def __eq__(self, other):
        if isinstance(other, int):
            return other == self.capacity
        elif isinstance(other, (Vegetarian, MeatEater)):
            return other.capacity == self.capacity
        else:
            return f'Невозможно сравнить количество сладкоежек с {other}'

    def __lt__(self, other):
        if isinstance(other, int):
            return self.capacity < other
        elif isinstance(other, (Vegetarian, MeatEater)):
            return self.capacity < other.capacity
        else:
            return f'Невозможно сравнить количество сладкоежек с {other}'

    def __gt__(self, other):
        if isinstance(other, int):
            return self.capacity > other
        elif isinstance(other, (Vegetarian, MeatEater)):
            return self.capacity > other.capacity
        else:
            return f'Невозможно сравнить количество сладкоежек с {other}'

p1 = Initialization('Chuck', [])
assert isinstance(p1, Initialization)
assert not hasattr(p1, 'capacity'), 'Не нужно создавать атрибут "capacity", если передается не целое число'
assert not hasattr(p1, 'food'), 'Не нужно создавать атрибут "food", если передается не целое число'

c1 = Vegetarian(100, [1, 2, 3])
print(c1)
assert isinstance(c1, Vegetarian)
assert c1.capacity == 100
assert c1.food == [1, 2, 3]

b1 = MeatEater(1000, ['Arkasha'])
print(b1)
assert isinstance(b1, MeatEater)
assert b1.capacity == 1000
assert b1.food == ['Arkasha']

pla = SweetTooth(444, [2150, 777])
print(pla)
assert isinstance(pla, SweetTooth)
assert pla.capacity == 444
assert pla.food == [2150, 777]
assert pla > 100
assert not pla < 80
assert not pla == 90
assert pla > c1
assert not pla < c1
assert not pla == c1
assert not pla > b1
assert pla < b1
assert not pla == b1

v_first = Vegetarian(10000, ['Орехи', 'овощи', 'фрукты'])
print(v_first)  # 10000 людей предпочитают не есть мясо! Они предпочитают ['Орехи', 'овощи', 'фрукты']
v_second = Vegetarian([23], ['nothing'])  # Количество людей должно быть целым числом

m_first = MeatEater(15000, ['Жареную картошку', 'рыба'])
print(m_first)  # 15000 мясоедов в Москве! Помимо мяса они едят еще и ['Жареную картошку', 'рыба']
s_first = SweetTooth(30000, ['Мороженое', 'Чипсы', 'ШОКОЛАД'])
print(s_first)  # Сладкоежек в Москве 30000. Их самая любимя еда: ['Мороженое', 'Чипсы', 'ШОКОЛАД']
print(s_first > v_first)  # Сладкоежек больше, чем людей с другим вкусовым предпочтением
print(30000 == s_first)  # Количество сладкоежек из опрошенных людей совпадает с 30000
print(s_first == 25000)  # Количество людей не совпадает
print(100000 < s_first)  # Количество сладкоежек в Москве не больше, чем 100000
print(100 < s_first)  # Количество сладкоежек больше, чем 100
