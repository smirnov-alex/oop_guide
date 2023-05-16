'''
class Vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

# Ниже расположен код для проверок, его не нужно удалять
modelX = Vehicle(200, 18000)
assert modelX.max_speed == 200
assert modelX.mileage == 18000
assert modelX.__dict__ == {'max_speed': 200, 'mileage': 18000}

audi = Vehicle(240, 5)
assert audi.__dict__ == {'max_speed': 240, 'mileage': 5}
print('Good')



class Laptop:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'{self.brand} {self.model}'
        return 'Hello'

print(Laptop(1, 2, 3))



class SoccerPlayer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0

    def score(self, today_goals=1):
        self.goals += today_goals

    def make_assists(self, today_assists):
        self.assists += today_assists

    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')


class Zebra():
    def __init__(self):
        self.flag = True

    def which_stripe(self):
        if self.flag:
            print('Полоска белая')
            self.flag = False
        else:
            print('Полоска черная')
            self.flag = True
'''


class Person:
    def __init__(self, name, surname, age):
        self.first_name = name
        self.last_name = surname
        self.age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name}'

    def is_adult(self):
        return self.age > 18

# Ниже код для проверки методов класса Person
p1 = Person('Ash', 'Ketchum', 20)
assert isinstance(p1, Person)
assert p1.full_name() == 'Ketchum Ash'
assert p1.age == 20
assert p1.first_name == 'Ash'
assert p1.last_name == 'Ketchum'
assert p1.is_adult() is True

p2 = Person('Hermione', 'Granger', 16)
assert isinstance(p2, Person)
assert p2.age == 16
assert p2.first_name == 'Hermione'
assert p2.last_name == 'Granger'
assert p2.full_name() == 'Granger Hermione'
assert p2.is_adult() is False
print('Good')
