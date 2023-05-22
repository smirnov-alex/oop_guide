# Магические методы. __str__ и __repr__
# __str__ - Для формирования строковых представлений экземпляров классов
# __repr__
class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'The object Lion - {self.name}'

    def __str__(self):
        return f'Lion - {self.name}'

q = Lion('Simba')
#print(q)
#print(f'{q!r}')


#task1
class Person:
    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        if gender not in ['male', 'female']:
            print("Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
            self.gender = 'male'
        else:
            self.gender = gender

    def __str__(self):
        if self.gender == 'male':
            return f"Гражданин {self.surname} {self.name}"
        else:
            return f"Гражданка {self.surname} {self.name}"

p1 = Person('Chuck', 'Norris')
#print(p1) # печатает "Гражданин Norris Chuck"
p2 = Person('Mila', 'Kunis', 'female')
#print(p2) # печатает "Гражданка Kunis Mila"
#p3 = Person('Оби-Ван', 'Кеноби', True)# печатает "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
#print(p3) # печатает "Гражданин Кеноби Оби-Ван"


# task2
class Vector:

    def __init__(self, *args):
        self.values = []
        for item in args:
            if isinstance(item, int) and not isinstance(item, bool):
                self.values.append(item)

    def __str__(self):
        if len(self.values) == 0:
            return f'Пустой вектор'

        return f'Вектор{str(tuple(sorted(self.values)))}'

v1 = Vector(5,1,2,3)
#print(v1) # печатает "Вектор(1, 2, 3)"
v2 = Vector()
#print(v2) # печатает "Пустой вектор"


# task3
class GroceryItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"""Name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}"""

    def __repr__(self):
        return f'GroceryItem({self.name}, {self.price}, {self.quantity})'


banana = GroceryItem('Banana', 10, 5)
assert banana.__str__() == """Name: Banana
Price: 10
Quantity: 5"""
assert repr(banana) == 'GroceryItem(Banana, 10, 5)'
print(banana)
print(f"{banana!r}")

dragon_fruit = GroceryItem('Dragon fruit', 5, 350)
assert dragon_fruit.__str__() == """Name: Dragon fruit
Price: 5
Quantity: 350"""
assert repr(dragon_fruit) == 'GroceryItem(Dragon fruit, 5, 350)'
print(dragon_fruit)
print(f"{dragon_fruit!r}")


