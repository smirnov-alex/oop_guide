'''
class BankAccount:

    def __init__(self, account, balance):
        self._account_number = account
        self._balance = balance

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance
    
    def set_balance(self, value):
        self._balance = value

account = BankAccount("1234567890", 1000)
assert account._balance == 1000
assert account._account_number == "1234567890"
assert account.get_account_number() == "1234567890"
assert account.get_balance() == 1000
account.set_balance(1500)
assert account.get_balance() == 1500

print('Good')




class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def __get_name(self):
        return self.__name
    
    def __get_salary(self):
        return self.__salary
    
    def __set_salary(self, value):
        if (not isinstance(value, (float, int))) or value < 0:
            print(f'ErrorValue:{value}')
        else:
            self.__salary = value

    title = property(fget=__get_name)
    reward = property(fget=__get_salary, fset=__set_salary)

'''


class UserMail:
    def __init__(self, login, address):
        self.login = login
        self.__email = address

    def get_email(self):
        return self.__email
    
    def set_email(self, address):
        if not isinstance(address, str):
            print(f'ErrorMail:{address}')
        else:            
            if address.count('@') == 1 and address.count('.') == 1:
                index_a = address.index('@')
                index_dot = address.index('.')
                if index_a < index_dot:
                    self.__email = address
                else:
                    print(f'ErrorMail:{address}')
            else:
                print(f'ErrorMail:{address}')

    email = property(fget=get_email, fset=set_email)

jim = UserMail("aka47", 'hello@com.org')
assert jim.login == "aka47"
assert jim._UserMail__email == "hello@com.org"
assert isinstance(jim, UserMail)
assert isinstance(type(jim).email, property), 'Вы не создали property email'

jim.email = [1, 2, 3]  # печатает ErrorMail:[1, 2, 3]
jim.email = 'hello@@re.ee'  # печатает ErrorMail:hello@@re.ee
jim.email = 'hello@re.w3'
assert jim.email == 'hello@re.w3'

k = UserMail('belosnezhka', 'prince@wait.you')
assert k.email == 'prince@wait.you'
assert k.login == 'belosnezhka'
assert isinstance(k, UserMail)

k.email = {1, 2, 3}  # печатает ErrorMail:{1, 2, 3}
k.email = 'prince@still@.wait'  # печатает ErrorMail:prince@still@.wait
k.email = 'prince@stillwait'  # печатает ErrorMail:prince@stillwait
k.email = 'prince@still.wait'
assert k.get_email() == 'prince@still.wait'
k.email = 'pri.nce@stillwait'  # печатает ErrorMail:pri.nce@stillwait
assert k.email == 'prince@still.wait'


