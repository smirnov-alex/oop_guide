# Property. Через декоратор @property

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):
        print('get balance')
        return self.__balance
    
    # my_property_balance = my_balance
    
    @my_balance.setter
    def my_balance(self, value):
        print('set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом!')
        self.__balance = value

    # my_balance = my_property_balance.setter(my_balance)
    
    @my_balance.deleter
    def my_balance(self):
        print('delete balance')
        del self.__balance

    # my_balance = property(my_balance)
    # my_balance = my_balance.getter(get_balance)
    # my_balance = my_balance.setter(set_balance)
    # my_balance = my_balance.deleter(delete_balance)

b = BankAccount('Misha', 150)
print(b.my_balance)
b.my_balance = 666
print(b.my_balance)
