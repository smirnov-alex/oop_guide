# магические методы
# __call__

# from time import perf_counter
import time


class Counter:

    def __init__(self):
        self.counter = 0
        self.summa = 0
        self.length = 0
        print('init object', self)

    def __call__(self, *args, **kwargs):
        self.counter += 1
        self.summa += sum(args)
        self.length += len(args)
        print(f'наш экземпляр вызывался {self.counter} раз')

    def average(self):
        return self.summa / self.length

# b = Counter()
# print(b.counter)
# print(b.summa)
# b(3, 4, 5)
# print(b.summa)
# print(b.length)
# b(1, 2)
# print(b.summa)
# print(b.length)
# print(b.average())
#
'''
class Timer:
    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print(f'Вызывается функция {self.fn.__name__}')
        result = self.fn(*args, **kwargs)
        finish = perf_counter()
        print(f'Функция отработала за {finish - start}')
        return result


@Timer
def fact(n):
    pr = 1
    for i in range(1, n+1):
        pr *= i
    return pr


def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

# fact = Timer(fact)
# print(fact(7))
# print(fact(7))

# fact = Timer(fib)
# print(fact(fib))
# print(fib(20))
# print(Timer(fib)(7))
'''

class QuadraticFunction:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return self.a * x * x + self.b * x + self.c

f = QuadraticFunction(2, 5, 7)
assert f(1) == 14
assert f(-3) == 10
assert f(2) == 25
assert f(5) == 82

f_2 = QuadraticFunction(-1, 2, 4)
assert f_2(5) == -11
assert f_2(2) == 4
assert f_2(-3) == -11
assert f_2(1) == 5
print('Good')


class Addition:
    def __call__(self, *args, **kwargs):
        summa = 0
        for item in args:
            if isinstance(item, (int, float)):
                summa += item
        return f'Сумма переданных значений = {summa}'

add = Addition()
assert add(10, 20) == "Сумма переданных значений = 30"
assert add(1, 2, 3.4) == "Сумма переданных значений = 6.4"
assert add(1, 2, 'hello', [1, 2], 3) == "Сумма переданных значений = 6"


add2 = Addition()
assert add2(10, 20, 3, 3, 4, 3, 2, 43, 43) == "Сумма переданных значений = 131"
assert add2() == "Сумма переданных значений = 0"
assert add2('hello') == "Сумма переданных значений = 0"

print('Good')


class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        start = time.time()
        self.func()
        finish = time. time()
        print(f'Время работы функции {finish - start}')

@Timer
def calculate():
    for i in range(10000000):
        2**100

calculate()
