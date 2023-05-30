# обработка исключений
try:
    # 1 / 0
    int('123')
    a + b
except ValueError:
    print('error ValueError')
except ZeroDivisionError:
    print('error ZeroDivisionError')
except NameError:
    print('error NameError')

s = 'hello'
d = {}
try:
    # s[6]
    d['key']
except LookupError:
    print('error IndexError')

try:
    4 + 'dfgd'
except Exception as ex:
    print(f'error: {ex.__class__.__name__}')
finally:
    print('end')

try:
    1/0
except (KeyError, IndexError):
    print('LookupError')
except ZeroDivisionError:
    print('ZeroDivisionError')
else:
    print('Good')
finally:
    print('end')

'''
try:
    a = int(input())
    b = int(input())
    a/b
except ValueError:
    print('Введите целое число')
except ZeroDivisionError:
    print('Делитель не должен быть равен нулю')
else:
    print(f"Результат деления a на b: {a/b}")
    '''

try:
    file = open('pentagon_secrets.txt', 'r')
    print(file.read())
except FileNotFoundError:
    print('Эх, не судьба тайны пентагона узнать')


def func(phrase):
    func(phrase)


try:
    func('Это рекурсия, детка!')
except RecursionError:
    print('Кто-то должен остановить это безумие')


class CustomButton:
    def __init__(self, text, **kwargs):
        self.text = text
        for key, value in kwargs.items():
            setattr(self, key, value)

    def config(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def click(self):
        try:
            self.command()
        except AttributeError:
            print('Кнопка не настроена')
        except TypeError:
            print('Кнопка сломалась')


def func():
    print('Оно живое')


btn = CustomButton(text="Hello", bd=20, bg='#ffaaaa')
btn.click()  # Кнопка не настроена
btn.config(command=func)
btn.click()  # Оно живое
