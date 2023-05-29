# Абстракция - это процесс выделения существенных характеристик объекта и игнорирования несущественных деталей.
# Абстракция используется в программировании для упрощения сложных задач и сокрытия деталей реализации.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        """Вносим деньги на счет"""
        pass

    def withdraw(self, amount):
        """Снимаем деньги со счета"""
        pass

    def get_balance(self):
        """Получаем доступный баланс"""
        pass

# Абстрактный класс - это класс, который не предназначен для создания объектов напрямую.
# Он является классом-шаблоном для других классов и определяет абстрактные методы,
# которые должны быть реализованы в дочерних классах.
# Абстрактный метод - это метод, который объявлен в абстрактном классе, но не имеет реализации.
# Он служит как бы шаблоном для метода, который должен быть реализован в подклассах.
# В Python абстрактные классы реализуются с помощью модуля abc (аббревиатура от Abstract Base Classes).
# Для создания абстрактного класса нам понадобиться класс ABC, а для создания абстрактного метода -
# декоратор abstractmethod. Оба эти объекта импортируются из стандартного модуля abc


from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# task1
class Employee:
    @abstractmethod
    def calculate_salary(self):
        pass


class HourlyEmployee(Employee):
    def __init__(self, hours_worked, hourly_rate):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class SalariedEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

hourly_employee = HourlyEmployee(100, 25)
assert hourly_employee.hours_worked == 100
assert hourly_employee.hourly_rate == 25
assert hourly_employee.calculate_salary() == 2500

salaried_employee = SalariedEmployee(4000)
assert salaried_employee.monthly_salary == 4000
assert salaried_employee.calculate_salary() == 4000
print('Good')


# task2
class Database:
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def execute(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print('Connecting to MySQL database...')

    def disconnect(self):
        print('Disconnecting from MySQL database...')

    def execute(self, query):
        print(f"Executing query '{query}' in MySQL database...")


class PostgreSQLDatabase(Database):
    def connect(self):
        print('Connecting to PostgreSQL database...')

    def disconnect(self):
        print('Disconnecting from PostgreSQL database...')

    def execute(self, query):
        print(f"Executing query '{query}' in PostgreSQL database...")

mysql_db = MySQLDatabase()
postgresql_db = PostgreSQLDatabase()

mysql_db.connect()
mysql_db.execute(
    "SELECT * FROM customers;")
mysql_db.disconnect()

postgresql_db.connect()
postgresql_db.execute(
    "SELECT * FROM customers;")
postgresql_db.disconnect()