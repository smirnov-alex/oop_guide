# Пользовательские исключения


class MyException(Exception):
    '''this is my first exception'''

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('__str__ called')
        if self.message:
            return f'My exception ({self.message})'
        else:
            return 'My exception is empty'


# try:
#     raise MyException('hello')
# except ArithmeticError:
#     print('done')

# raise MyException('hello', 42)


# task1
users = {
    "alice": {"name": "Alice Smith", "email": "alice@example.com"},
    "bob": {"name": "Bob Johnson", "email": "bob@example.com"},
    "jack": {"name": "Jack Wild", "email": "jack_wild@example.com"}
}

class UserNotFoundError(Exception):
    def __str__(self):
        return 'User not found'


def get_user(username):
    if username not in users.keys():
        raise UserNotFoundError()
    return users[username]['name']

# try:
#     username = get_user(input())
# except UserNotFoundError as e:
#     print(e)
# else:
#     print(username)


# task2
class NegativeDepositError(Exception):
    def __str__(self):
        return "Нельзя пополнить счет отрицательным значением"


class InsufficientFundsError(Exception):
    def __str__(self):
        return "Недостаточно средств для снятия"


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, value):
        if value < 0:
            raise NegativeDepositError()
        else:
            self.balance += value

    def withdraw(self, value):
        if value > self.balance:
            raise InsufficientFundsError()
        else:
            self.balance -= value

try:
    raise InsufficientFundsError("Недостаточно средств")
except Exception as e:
    if not isinstance(e, InsufficientFundsError):
        raise ValueError('Реализуйте исключение InsufficientFundsError')

try:
    raise NegativeDepositError("Внесено отрицательное значение")
except Exception as e:
    if not isinstance(e, NegativeDepositError):
        raise ValueError('Реализуйте исключение NegativeDepositError')

account = BankAccount(100)
assert account.balance == 100

account.deposit(50)
assert account.balance == 150

account.withdraw(75)
assert account.balance == 75

try:
    account.withdraw(100)
except InsufficientFundsError as e:
    print(e)  # "Недостаточно средств"

assert account.balance == 75

try:
    account.deposit(-50)
except NegativeDepositError as e:
    print(e)  # "Внесено отрицательное значение"


# task3
class PasswordInvalidError(Exception):
    pass


class PasswordLengthError(PasswordInvalidError):
    def __str__(self):
        return "Пароль должен быть не менее 8 символов"


class PasswordContainUpperError(PasswordInvalidError):
    def __str__(self):
        return "Пароль должен содержать хотя бы одну заглавную букву"


class PasswordContainDigitError(PasswordInvalidError):
    def __str__(self):
        return "Пароль должен содержать хотя бы одну цифру"


class User:
    def __init__(self, username, password=None):
        self.username = username
        self.password = password

    def set_password(self, value):
        if len(value) < 8:
            raise PasswordLengthError()
        result_upper = []
        for item in value:
            letter = item.isupper()
            result_upper.append(letter)
        if not any(result_upper):
            raise PasswordContainUpperError()
        result_digit = []
        for item2 in value:
            letter2 = item2.isdigit()
            result_digit.append(letter2)
        if not any(result_digit):
            raise PasswordContainDigitError()
        self.password = value

assert issubclass(PasswordInvalidError, Exception)
assert issubclass(PasswordLengthError, PasswordInvalidError)
assert issubclass(PasswordContainUpperError, PasswordInvalidError)
assert issubclass(PasswordContainDigitError, PasswordInvalidError)

user = User("johndoe")

try:
    user.set_password("weakpwd")
except PasswordLengthError as e:
    print(e)

try:
    user.set_password("strongpassword8")
except PasswordContainUpperError as e:
    print(e)

try:
    user.set_password("Safepassword")
except PasswordContainDigitError as e:
    print(e)

user.set_password("SecurePass123")
assert user.password == 'SecurePass123'