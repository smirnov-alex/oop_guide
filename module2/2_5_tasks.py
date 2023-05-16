'''
class BankDeposit:
    def __init__(self, name, balance, rate):
        self.name = name
        self.balance = balance
        self.rate = rate

    def __calculate_profit(self):
        return self.balance * self.rate / 100

    def get_balance_with_profit(self):
        return self.__calculate_profit() + self.balance

account = BankDeposit("John Connor", 1000, 5)
assert account.name == "John Connor"
assert account.balance == 1000
assert account.rate == 5
print(account._BankDeposit__calculate_profit())
assert account._BankDeposit__calculate_profit() == 50.0
assert account.get_balance_with_profit() == 1050.0

account_2 = BankDeposit("Sarah Connor", 200, 27)
assert account_2.name == "Sarah Connor"
assert account_2.balance == 200
assert account_2.rate == 27
assert account_2._BankDeposit__calculate_profit() == 54.0
assert account_2.get_balance_with_profit() == 254.0
print('Good')



class Library:
    def __init__(self, books):
        self.__books = books

    def __check_availability(self, name):
        return name in self.__books

    def search_book(self, name):
        return (self.__check_availability(name))
    
    def return_book(self, name):
        self.__books.append(name)

    def _checkout_book(self, name):
        if self.search_book(name):
            self.__books.remove(name)
            return True
        else:
            return False

library = Library(["War and Peace", "Moby-Dick", "Pride and Prejudice"])

assert library._Library__books == ["War and Peace", "Moby-Dick", "Pride and Prejudice"]
assert library.search_book("Moby-Dick") == True
assert library.search_book("Jane Air") == False

assert library._Library__check_availability("War and Peace") == True
assert library._checkout_book("Moby-Dick") == True
assert library._Library__books == ["War and Peace", "Pride and Prejudice"]

assert library.search_book("Moby-Dick") == False
assert library.return_book("Moby-Dick") is None
assert library._Library__books == ["War and Peace", "Pride and Prejudice", "Moby-Dick"]
assert library.search_book("Moby-Dick") == True
print('Good')
'''


class Employee:
    def __init__(self, name, position, hours_worked, hourly_rate):
        self.name = name
        self.__position = position
        self.__hours_worked = hours_worked
        self.__hourly_rate = hourly_rate

    def __calculate_salary(self):
        return self.__hourly_rate * self.__hours_worked
    
    def _set_position(self, position):
        self.__position = position

    def get_position(self):
        return self.__position
    
    def get_salary(self):
        return self.__calculate_salary()
    
    def get_employee_details(self):
        result = f"Name: {self.name}, Position: {self.get_position()}, Salary: {self.get_salary()}"
        return result

employee = Employee("Джеки Чан", 'manager', 20, 40)
assert employee.name == 'Джеки Чан'
assert employee._Employee__hours_worked == 20
assert employee._Employee__hourly_rate == 40
assert employee._Employee__position == 'manager'
assert employee.get_position() == 'manager'
assert employee.get_salary() == 800
assert employee._Employee__calculate_salary() == 800
assert employee.get_employee_details() == 'Name: Джеки Чан, Position: manager, Salary: 800'
employee._set_position('Director')
assert employee.get_employee_details() == 'Name: Джеки Чан, Position: Director, Salary: 800'

employee_2 = Employee("Пирс Броснан", 'actor', 35, 30)
assert employee_2._Employee__calculate_salary() == 1050
assert employee_2.get_employee_details() == 'Name: Пирс Броснан, Position: actor, Salary: 1050'

print('Good')