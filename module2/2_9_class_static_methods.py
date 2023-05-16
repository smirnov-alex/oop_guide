# classmethod и staticmethod

class Example:
    def hello():
        print('hello')

    def instance_hello(self):
        print(f'instance hello {self}')

    @staticmethod
    def static_hello():
        print('static hello')

    @classmethod
    def class_hello(cls):
        print(f'class hello {cls}')

Example.hello()
a = Example()
# ошибка, так как метод принимает один аргумент по умолчанию (экземпляр класса)
# a.hello()
a.instance_hello()

# после определения статик метода, его можно вызывать как от класса так и от экземпляра
Example.static_hello()
a.static_hello()

Example.class_hello()
a.class_hello()


# Метод @classmethod также можно использовать в качестве метода для создания нового экземпляра класса.
class Car:

    def __init__(self, model, color):
        self.model = model
        self.color = color

    @classmethod
    def get_red_car(cls, model):
        return cls(model, 'red')


car1 = Car.get_red_car('Audi')
print(car1, car1.model, car1.color)

car2 = Car.get_red_car('BMW')
print(car2, car2.model, car2.color)
