# практика по property и методам класса
from string import digits

class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__secret = '4 8 15 16 23 42'

    @property
    def password(self):
        print('getter called')
        return self.__password

    @property
    def secret(self):
        s = input('Введите ваш пароль: ')
        if s == self.password:
            return self.__secret
        else:
            raise ValueError('Доступ закрыт, неверный пароль!')

    @staticmethod
    def is_include_number(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @password.setter
    def password(self, value):
        print('setter called')
        if not isinstance(value, str):
            raise TypeError("Пароль должен быть строкой")
        if len(value) < 4:
            raise ValueError("Длина пароля слишком мала, минимум четыре символа")
        if len(value) > 12:
            raise ValueError("Длина пароля слишком велика, максимум 12 символов")
        if not User.is_include_number(value):
            raise ValueError("Пароль должен содержать хотя бы одну цифру")
        self.__password = value



q = User('aaa', 12345)
q.password
