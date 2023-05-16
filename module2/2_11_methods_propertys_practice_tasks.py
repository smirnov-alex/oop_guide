'''
from string import digits, ascii_lowercase, ascii_uppercase, ascii_letters


class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @staticmethod
    def is_include_only_latin(password):
        flag = True
        for letter in password:
            if letter.isalpha() and letter not in ascii_letters:
                flag = False
        return flag

    @staticmethod
    def check_password_dictionary(password):
        passwords = []
        with open('easy_passwords.txt', 'r') as file:
            for elem in file:
                passwords.append(elem.strip())
        if password in passwords:
            return True
        else:
            return False

    @staticmethod
    def is_include_all_register(password):
        flag_lower = False
        flag_upper = False
        for letter in ascii_lowercase:
            if letter in password:
                flag_lower = True
        for letter in ascii_uppercase:
            if letter in password:
                flag_upper = True
        if flag_upper and flag_lower:
            return True
        return False

    @staticmethod
    def is_include_number(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        if not isinstance(value, str):
            raise TypeError()
        if value.count('@') != 1:
            raise ValueError()
        if value.count('.') != 1:
            raise ValueError()
        index_a = value.index('@')
        index_dot = value.index('.')
        if index_a > index_dot:
            raise ValueError()
        self.__login = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError("Пароль должен быть строкой")
        if len(value) < 5 or len(value) > 12:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not Registration.is_include_number(value):
            raise ValueError("Пароль должен содержать хотя бы одну цифру")
        if not Registration.is_include_all_register(value):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        if not Registration.is_include_only_latin(value):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        if Registration.check_password_dictionary(value):
            raise ValueError('Ваш пароль содержится в списке самых легких')
        self.__password = value

r1 = Registration('qwerty@rambler.ru', 'QwrRt124') # здесь хороший логин
print(r1.login, r1.password)  # qwerty@rambler.ru QwrRt124

# теперь пытаемся запись плохие пароли
r1.password = '123456'  # ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
r1.password = 'LoW'  # raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
r1.password = 43  # raise TypeError("Пароль должен быть строкой")



class File:
    def __init__(self, name):
        self.name = name
        self.in_trash = False
        self.is_deleted = False

    def restore_from_trash(self):
        self.in_trash = False
        print(f'Файл {self.name} восстановлен из корзины')

    def remove(self):
        self.is_deleted = True
        print(f'Файл {self.name} был удален')

    def read(self):
        if self.is_deleted:
            print(f'ErrorReadFileDeleted({self.name})')
            return
        if self.in_trash:
            print(f'ErrorReadFileTrashed({self.name})')
            return
        print(f'Прочитали все содержимое файла {self.name}')

    def write(self, content):
        if self.is_deleted:
            print(f'ErrorWriteFileDeleted({self.name})')
            return
        if self.in_trash:
            print(f'ErrorWriteFileTrashed({self.name})')
            return
        print(f'Записали значение {content} в файл {self.name}')


class Trash:
    content = []

    @staticmethod
    def add(file):
        if not isinstance(file, File):
            print('В корзину добавлять можно только файл')
            return
        Trash.content.append(file)
        file.in_trash = True

    @staticmethod
    def clear():
        print('Очищаем корзину')
        for item in Trash.content:
            item.remove()
        Trash.content = []
        print('Корзина пуста')

    @staticmethod
    def restore():
        print('Восстанавливаем файлы из корзины')
        for item in Trash.content:
            item.restore_from_trash()
        Trash.content = []
        print('Корзина пуста')
'''


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class User:
    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.balance}'

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def deposit(self, value):
        self.balance += value

    def payment(self, value):
        if value > self.balance:
            print('Не хватает средств на балансе. Пополните счет')
            return False
        else:
            self.balance = self.balance - value
            return True


class Cart:
    def __init__(self, user):
        if isinstance(user, User):
            self.user = user
        self.goods = {}
        self.__total = 0

    def add(self, product, amount=1):
        self.goods[product] = self.goods.get(product, 0) + amount
        self.__total += product.price * amount

    def remove(self, product, amount=1):
        if self.goods[product] < amount:
            self.__total -= product.price * self.goods[product]
            del self.goods[product]
            return
        self.goods[product] = self.goods.get(product, 0) - amount
        self.__total -= product.price * amount

    @property
    def total(self):
        return self.__total

    def order(self):
        if self.user.payment(self.total):
            print('Заказ оплачен')
        else:
            print('Проблема с оплатой')

    def print_check(self):
        print('---Your check---')
        list_of_goods = sorted(self.goods.items(), key=lambda x: x[0].name)
        for key, value in list_of_goods:
            print(key.name, key.price, value, key.price * value)
        print(f'---Total: {self.total}---')


billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user) # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 2 40
---Total: 70---'''
cart_billy.add(lemon, 3)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.remove(lemon, 6)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
---Total: 30---'''
print(cart_billy.total) # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.order()
''' Печатает текст ниже
Не хватает средств на балансе. Пополните счет
Проблема с оплатой'''
cart_billy.user.deposit(150)
cart_billy.order() # Заказ оплачен
print(cart_billy.user.balance) # 20
