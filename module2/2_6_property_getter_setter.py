# Property. Getter-метод и setter-метод.

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом!')
        self.__balance = value

    def delete_balance(self):
        del self.__balance

    balance = property(fget=get_balance, fset=set_balance,fdel=delete_balance)


b = BankAccount('Vasya', 200)
# print(b.__balance)
b.__balance = 300
print(b.get_balance())
b.set_balance(400)
print(b.get_balance())
# b.set_balance('hello')
print(b.get_balance())
# проверяем работу property
print(b.balance)
b.balance = 500
print(b.balance)
# удаление свойства через property
client = BankAccount('Ivan', 100)
print(client.balance)
del client.balance
print(client.__dict__)
client.balance = 1234
print(client.__dict__)