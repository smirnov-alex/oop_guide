# Магические методы. Математические операции
# __add__ сложение
# __mul__ умножение
# __sub__ вычитание
# __truediv__ деление


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        print('__add__ call')
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        if isinstance(other, (int, float)):
            return self.balance + other
        raise NotImplemented

    def __radd__(self, other):
        print('__radd__ call')
        return self + other

    def __mul__(self, other):
        print('__mul__ call')
        if isinstance(other, BankAccount):
            return self.balance * other.balance
        if isinstance(other, (int, float)):
            return self.balance * other
        if isinstance(other, str):
            return self.name + other
        raise NotImplemented


a = BankAccount('Misha', 500)
b = BankAccount('Ivan', 900)
# __add__
# print(b + 12)
# print(a + b)
# print(a + 'asdf') # raise
# print (12 + b)  # __radd__ => __add__
# __mul__
# print(a * 10)
# print(a * b)
# print(a * 'spam')


class Account:
    def __init__(self, name, balance):
        print('new obj init')
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f'Клиент {self.name} с балансом {self.balance}'

    def __add__(self, other):
        print('__add__ call')
        if isinstance(other, Account):
            return self.balance + other.balance
        if isinstance(other, (int, float)):
            return Account(self.name, self.balance + other)
        raise NotImplemented

a = Account('Misha', 500)


class Example:
    def __init__(self):
        self.name = 'p'

a = Example()
b = Example()
#print(a + b)


class MyPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return MyPoint(2 * self.x + other.x, 2 * self.y + other.y)


p1 = MyPoint(3, 4)
p2 = MyPoint(5, 12)
p3 = p1 + p2
# print(p3.x + p3.y)


class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.width + other.width, self.height + other.height)

    def __str__(self):
        return f'Rectangle({self.width}x{self.height})'

r1 = Rectangle(5, 10)
assert r1.width == 5
assert r1.height == 10
# print(r1)

r2 = Rectangle(20, 5)
assert r2.width == 20
assert r2.height == 5
# print(r2)

r3 = r2 + r1
assert isinstance(r3, Rectangle)
assert r3.width == 25
assert r3.height == 15
# print(r3)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y


v1 = Vector(2, 3)
v2 = Vector(4, 3)
# print(v1 * v2)


class Order:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __add__(self, other):
        return Order(self.cart + [other], self.customer)

    def __radd__(self, other):
        return Order([other] + self.cart, self.customer)

    def __sub__(self, other):
        if other in self.cart:
            self.cart.remove(other)
            return Order(self.cart, self.customer)
        else:
            return Order(self.cart, self.customer)

    def __rsub__(self, other):
        if other in self.cart:
            self.cart.remove(other)
            return Order(self.cart, self.customer)
        else:
            return Order(self.cart, self.customer)

order = Order(['banana', 'apple'], 'Гена Букин')

order_2 = order + 'orange'
assert order.cart == ['banana', 'apple']
assert order.customer == 'Гена Букин'
assert order_2.cart == ['banana', 'apple', 'orange']

order = 'mango' + order
assert order.cart == ['mango', 'banana', 'apple']
order = 'ice cream' + order
assert order.cart == ['ice cream', 'mango', 'banana', 'apple']

order = order - 'banana'
assert order.cart == ['ice cream', 'mango', 'apple']

order3 = order - 'banana'
assert order3.cart == ['ice cream', 'mango', 'apple']

order = order - 'mango'
assert order.cart == ['ice cream', 'apple']
order = 'lime' - order
assert order.cart == ['ice cream', 'apple']
print('Good')


class Vector:
    def __init__(self, *args):
        self.values = []
        for item in args:
            if isinstance(item, int) and not isinstance(item, bool):
                self.values.append(item)
        self.values = sorted(self.values)

    def __str__(self):
        if len(self.values) == 0:
            return f'Пустой вектор'
        return f'Вектор{tuple(self.values)}'

    def __add__(self, other):
        if isinstance(other, Vector):
            if len(other.values) == len(self.values):
                new_values = []
                for i in range(len(self.values)):
                    new_item = self.values[i] + other.values[i]
                    new_values.append(new_item)
                return Vector(*new_values)
            else:
                print("Сложение векторов разной длины недопустимо")
        elif isinstance(other, int):
            new_values = []
            for item in self.values:
                new_item = item + other
                new_values.append(new_item)
            return Vector(*new_values)
        else:
            print(f"Вектор нельзя сложить с {other}")

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(other.values) == len(self.values):
                new_values = []
                for i in range(len(self.values)):
                    new_item = self.values[i] * other.values[i]
                    new_values.append(new_item)
                return Vector(*new_values)
            else:
                print("Умножение векторов разной длины недопустимо")
        elif isinstance(other, int):
            new_values = []
            for item in self.values:
                new_item = item * other
                new_values.append(new_item)
            return Vector(*new_values)
        else:
            print(f"Вектор нельзя умножать с {other}")

v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"

v2 = Vector(3,4,5)
print(v2) # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3) # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4) # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5) # печатает "Вектор(2, 4, 6)"
v1 + 'hi' # печатает "Вектор нельзя сложить с hi"