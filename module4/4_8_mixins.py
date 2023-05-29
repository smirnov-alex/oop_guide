# Миксины

class Mixin:
    def mixin_method(self):
        print("This is a mixin method.")


class MyClass(Mixin):
    def my_method(self):
        self.mixin_method()

obj = MyClass()
obj.my_method()  # Output: This is a mixin method.


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f'{self.name} is eating.')

    def sleep(self):
        print(f'{self.name} is sleeping.')


class FlyingMixin:
    def fly(self):
        print(f'{self.name} is flying.')


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, 'dog')
        self.breed = breed

    def bark(self):
        print('Woof!')


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, 'cat')
        self.color = color

    def meow(self):
        print('Meow!')


class Bat(Animal, FlyingMixin):
    def __init__(self, name):
        super().__init__(name, 'bat')


class FlyingSquirrel(Animal, FlyingMixin):
    def __init__(self, name):
        super().__init__(name, 'flying squirrel')

b = Bat('Dracula')
b.fly()  # выведет "Dracula is flying."


# task1
class BasePizza:
    BASE_PIZZA_PRICE = 15

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.toppings = ['cheese']

    def __str__(self):
        return f"{self.name} with {self.toppings}, ${self.price:.2f}"


class PepperoniMixin:
    def add_pepperoni(self):
        print("Adding pepperoni!")
        self.price += 5
        self.toppings += ['pepperoni']


class MushroomMixin:
    def add_mushrooms(self):
        print("Adding mushrooms!")
        self.price += 3
        self.toppings += ['mushrooms']


class OnionMixin:
    def add_onion(self):
        print("Adding onion!")
        self.price += 2
        self.toppings += ['onion']


class BaconMixin:
    def add_bacon(self):
        print("Adding bacon!")
        self.price += 6
        self.toppings += ['bacon']


class OlivesMixin:
    def add_olives(self):
        print("Adding olives!")
        self.price += 1
        self.toppings += ['olives']


class HamMixin:
    def add_ham(self):
        print("Adding ham!")
        self.price += 7
        self.toppings += ['ham']


class PepperMixin:
    def add_pepper(self):
        print("Adding pepper!")
        self.price += 3
        self.toppings += ['pepper']


class ChickenMixin:
    def add_chicken(self):
        print("Adding chicken!")
        self.price += 5
        self.toppings += ['chicken']


class OlivesPizza(BasePizza, OlivesMixin):

    def __init__(self):
        super().__init__('Море оливок', BasePizza.BASE_PIZZA_PRICE)
        self.add_olives()


class PepperoniPizza(BasePizza, PepperoniMixin):

    def __init__(self):
        super().__init__('Колбасятина', BasePizza.BASE_PIZZA_PRICE)
        self.add_pepperoni()


class MushroomOnionBaconPizza(BasePizza, MushroomMixin, OnionMixin, BaconMixin):

    def __init__(self):
        super().__init__('Грибной пяточок с луком', BasePizza.BASE_PIZZA_PRICE)
        self.add_mushrooms()
        self.add_onion()
        self.add_bacon()


class CountryPizza(BasePizza, HamMixin, PepperMixin, OlivesMixin, PepperoniMixin, MushroomMixin, ChickenMixin):

    def __init__(self):
        super().__init__('Деревенская пицца', BasePizza.BASE_PIZZA_PRICE)
        self.add_ham()
        self.add_pepper()
        self.add_olives()
        self.add_pepperoni()
        self.add_mushrooms()
        self.add_chicken()


# Создайте экземпляр CountryPizza в переменной pizza
# pizza = CountryPizza()


# Код для проверки

# assert pizza.name == 'Деревенская пицца'
# assert pizza.price == 39
# assert pizza.toppings == ['cheese', 'ham', 'pepper', 'olives', 'pepperoni', 'mushrooms', 'chicken']
# print(pizza)


# task2
class PermissionMixin:

    def __init__(self):
        self.permissions = set()

    def grant_permission(self, permission):
        self.permissions.add(permission)

    def revoke_permission(self, permission):
        self.permissions.discard(permission)

    def has_permission(self, permission):
        return permission in self.permissions


class User(PermissionMixin):

    def __init__(self, name, email):
        super().__init__()
        self.name = name
        self.email = email

user1 = User('Alice', 'alice@example.com')
user2 = User('Bob', 'bob@example.com')

assert user1.email == 'alice@example.com'
assert user1.name == 'Alice'
assert user1.permissions == set()

assert user2.email == 'bob@example.com'
assert user2.name == 'Bob'
assert user2.permissions == set()

user1.grant_permission('read')
user1.grant_permission('write')
user2.grant_permission('read')
assert user1.permissions == {'read', 'write'}
assert user2.permissions == {'read'}

assert user1.has_permission('read') is True
assert user1.has_permission('write') is True
assert user1.has_permission('execute') is False

assert user2.has_permission('read') is True
assert user2.has_permission('write') is False
assert user2.has_permission('execute') is False

user1.revoke_permission('write')
user1.revoke_permission('execute')

assert user1.has_permission('read') is True
assert user1.has_permission('write') is False
assert user1.has_permission('execute') is False

print('Good')

# task3


# Напишите определение класса JsonSerializableMixin
import json


class JsonSerializableMixin:
    def to_json(self):
        return json.dumps(self.__dict__)


# Ниже код для проверки миксина JsonSerializableMixin
class Car(JsonSerializableMixin):
    def __init__(self, make: str, color: str):
        self.make = make
        self.color = color


class Book(JsonSerializableMixin):
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author


class Person(JsonSerializableMixin):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


car = Car("Toyota", "red")
print(car.to_json())
assert car.to_json() == '{"make": "Toyota", "color": "red"}'
book = Book("The Catcher in the Rye", "J.D. Salinger")
assert book.to_json() == '{"title": "The Catcher in the Rye", "author": "J.D. Salinger"}'
book.ratings = [5, 4, 5, 4, 5]
book.is_bestseller = True
book.to_json() == '{"title": "The Catcher in the Rye", "author": "J.D. Salinger", ' \
                  '"ratings": [5, 4, 5, 4, 5], "is_bestseller": true}'
person = Person("John", 30)
assert person.to_json() == '{"name": "John", "age": 30}'
print('Good')
