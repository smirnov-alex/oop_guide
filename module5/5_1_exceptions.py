# Exceptions in Python

# print('hello')
# try:
#     int('hello2')  # ValueError: invalid literal for int() with base 10: 'hello3'
# except ValueError:
#     print('Неправильный тип данных')
#     print('hello3')  # IndentationError: unexpected indent
# 1 / 0  # ZeroDivisionError: division by zero
# a + b  # NameError: name 'a' is not defined
# 'hello'[9]  # IndexError: string index out of range
# print('hello')


# task1
class Wallet:
    def __init__(self, currency, balance):
        if not isinstance(currency, str):
            raise TypeError("Неверный тип валюты")
        if not len(currency) == 3:
            raise NameError("Неверная длина названия валюты")
        if not currency.isupper():
            raise ValueError("Название должно состоять только из заглавных букв")
        self.currency = currency
        self.balance = balance

    def __eq__(self, other):
        if not isinstance(other, Wallet):
            raise TypeError(f"Wallet не поддерживает сравнение с {other}")
        if not self.currency == other.currency:
            raise ValueError("Нельзя сравнить разные валюты")
        return self.balance == other.balance

    def __add__(self, other):
        if not isinstance(other, Wallet):
            raise ValueError("Данная операция запрещена")
        if not self.currency == other.currency:
            raise ValueError("Данная операция запрещена")
        return Wallet(self.currency, self.balance + other.balance)

    def __sub__(self, other):
        if not isinstance(other, Wallet):
            raise ValueError("Данная операция запрещена")
        if not self.currency == other.currency:
            raise ValueError("Данная операция запрещена")
        return Wallet(self.currency, self.balance - other.balance)


wallet1 = Wallet('USD', 50)
wallet2 = Wallet('RUB', 100)
wallet3 = Wallet('RUB', 150)
# wallet4 = Wallet(12, 150)  # исключение TypeError('Неверный тип валюты')
# wallet5 = Wallet('qwerty', 150)  # исключение NameError('Неверная длина названия валюты')
# wallet6 = Wallet('abc', 150)  # исключение ValueError('Название должно состоять только из заглавных букв')
print(wallet2 == wallet3)  # False
# print(wallet2 == 100)  # TypeError('Wallet не поддерживает сравнение с 100')
# print(wallet2 == wallet1)  # ValueError('Нельзя сравнить разные валюты')
wallet7 = wallet2 + wallet3
# print(wallet7.currency, wallet7.balance)  # печатает 'RUB 250'
wallet2 + 45  # ValueError('Данная операция запрещена')