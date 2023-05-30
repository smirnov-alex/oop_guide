# raise
# er = Exception('Big error')
# raise er

# try:
#     {}['key']
# except (KeyError, IndexError) as error:
#     print(f"Logging error: {repr(error)}")
#     raise TypeError('ошибка типа') from None
#     # raise TypeError('ошибка типа') from error
# except ZeroDivisionError as err:
#     print('ZeroDivisionError')
#     print(f"Logging error: {err} {repr(err)}")


# try:
#     raise ValueError('ошибка значения')
# except ValueError:
#     try:
#         raise TypeError('ошибка типа')
#     except TypeError:
#         raise Exception('Большое исключение')


# task1
class Customer:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    @staticmethod
    def check_type(value):
        if not isinstance(value, (int, float)):
            raise TypeError('Банк работает только с числами')

    def withdraw(self, value):
        try:
            self.check_type(value)
        except TypeError as err:
            print(err)
        else:
            if self.balance >= value:
                self.balance -= value
            else:
                raise ValueError('Сумма списания превышает баланс')

    def deposit(self, value):
        self.check_type(value)
        self.balance += value

assert Customer.check_type(2) is None, 'Метод check_type не должен ничего возращать'
assert Customer.check_type(2.5) is None, 'Метод check_type не должен ничего возращать'

for i in ['hello', [1, 2, 3], dict(), set()]:
    try:
        Customer.check_type(i)
    except TypeError as error:
        print(error)
    else:
        raise TypeError(f'Метод check_type должен вызывать ошибку если передать {i}')

bob = Customer('Bob Odenkirk')
assert bob.balance == 0
assert bob.name == 'Bob Odenkirk'
try:
    bob.deposit('hello')
except TypeError as error:
    print(error)
else:
    raise ValueError("Нельзя вносить на счет баланса строку")

try:
    bob.deposit([])
except TypeError as error:
    print(error)
else:
    raise ValueError("Нельзя вносить на счет баланса список")

bob.deposit(200)
assert bob.balance == 200

try:
    bob.withdraw(300)
except ValueError as e:
    print(e)
else:
    raise ValueError("Проверьте списание при превышении лимита")

bob.withdraw(150)
assert bob.balance == 50

terk = Customer('Terk', 1000)
assert terk.name == 'Terk'
assert terk.balance == 1000
terk.withdraw(999)
assert terk.balance == 1, 'Не списались деньги, проверяйте списание'
terk.withdraw(1)
assert terk.balance == 0, 'Не списались деньги, проверяйте списание'

try:
    terk.withdraw(1)
except ValueError as e:
    print(e)
else:
    raise ValueError("Проверьте списание при превышении лимита")
assert terk.balance == 0


# task2
def sum_numbers(numbers):
    if not isinstance(numbers, list):
        raise TypeError('Аргумент numbers должен быть списком')
    if len(numbers) == 0:
        raise ValueError("Пустой список")
    for item in numbers:
        if not isinstance(item, (int, float)):
            raise TypeError('Неправильный тип элемента')
    return sum(numbers)

for value in (True, (1, 2, 3), {1: 'hello'}, {1, 2, 3}):
    try:
        result = sum_numbers(value)
    except TypeError as error:
        print(error)

try:
    result = sum_numbers([])
except ValueError as error:
    print(error)

try:
    sum_numbers([1, 'hello', 2, 3])
except TypeError as error:
    print(error)

try:
    sum_numbers([1, 2, 3, 4, 5, [1, 2, 3]])
except TypeError as error:
    print(error)

try:
    sum_numbers([1, 2, 3, 4, 5, {1, 2, 3}])
except TypeError as error:
    print(error)

try:
    sum_numbers([1, 2, 3, 4, 5, (1, 2, 3)])
except TypeError as error:
    print(error)

assert sum_numbers([1, 2, 3, 4, 5]) == 15
assert sum_numbers([1, 2, 3, 4, 5.0]) == 15.0