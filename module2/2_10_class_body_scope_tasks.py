# пространство имен класса

'''
class MyClass:
    class_attribute = "I am a class attribute"

    def __init__(self):
        self.instance_attribute = "I am an instance attribute"

    @classmethod
    def create_attr(cls, attr_name, attr_value):
        setattr(cls, attr_name, attr_value)


example_1 = MyClass()
example_2 = MyClass()
example_3 = MyClass()

example_1.create_attr('new_attr', "Hello world")

print(example_1.new_attr)
print(example_2.new_attr)
print(example_3.new_attr)



class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        Robot.population += 1
        print(f"Робот {self.name} был создан")

    def destroy(self):
        Robot.population -= 1
        print(f"Робот {self.name} был уничтожен")

    def say_hello(self):
        print(f"Робот {self.name} приветствует тебя, особь человеческого рода")

    @classmethod
    def how_many(cls):
        print(f"{cls.population}, вот сколько нас еще осталось")

r2 = Robot("R2-D2") # печатает "Робот R2-D2 был создан"
r2.say_hello() # печатает "Робот R2-D2 приветствует тебя, особь человеческого рода"
Robot.how_many() # печатает "1, вот сколько нас еще осталось"
r2.destroy() # печатает "Робот R2-D2 был уничтожен"



class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role


class Access:
    __access_list = ['admin', 'developer']

    @staticmethod
    def __check_access(role):
        return role in Access.__access_list

    @staticmethod
    def get_access(user):
        if not isinstance(user, User):
            print('AccessTypeError')
            return
        if Access.__check_access(user.role):
            print(f"User {user.name}: success")
        else:
            print("AccessDenied")

user1 = User('batya99', 'admin')
Access.get_access(user1) # печатает "User batya99: success"

zaya = User('milaya_zaya999', 'user')
Access.get_access(zaya) # печатает AccessDenied

Access.get_access(5) # печатает AccessTypeError
'''

class BankAccount:
    bank_name = 'Tinkoff Bank'
    address = "Москва, ул. 2-я Хуторская, д. 38А"

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    @classmethod
    def create_account(cls, name, balance):
        return cls(name, balance)

    @classmethod
    def bank_info(cls):
        return f"{cls.bank_name} is located in {cls.address}"

oleg = BankAccount.create_account("Олег Тинкофф", 1000)
assert isinstance(oleg, BankAccount)
assert oleg.name == 'Олег Тинкофф'
assert oleg.balance == 1000
assert BankAccount.bank_info() == 'Tinkoff Bank is located in Москва, ул. 2-я Хуторская, д. 38А'

ivan = BankAccount.create_account("Ivan Reon", 50)
assert isinstance(ivan, BankAccount)
assert ivan.name == 'Ivan Reon'
assert ivan.balance == 50
print('Good')
