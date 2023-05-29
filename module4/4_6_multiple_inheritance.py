# множественное наследование


class Doctor:

    def __init__(self, degree):
        self.degree = degree

    def graduate(self):
        print('Ура, я отучился на доктора')

    def can_build(self):
        print('Я доктор, я тоже немного умею строить')


class Builder:

    def __init__(self, rank):
        self.rank = rank

    def can_build(self):
        print('Я строитель, я умею строить')

    def graduate(self):
        print('Ура, я отучился на строителя')


class Person(Builder, Doctor):

    def __init__(self, rank, degree):
        super().__init__(rank)
        Doctor.__init__(self, degree)

    def __str__(self):
        return f'Person {self.rank} {self.degree}'

    def graduate(self):
        print('Посмотрим, кем я стал')
        super().graduate()
        Doctor.graduate(self)

print(Person.__mro__)
p = Person(5, 'spec')
print(p)


# task1
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_info(self):
        return f'Имя пользователя: {self.username}'


class Authentication:
    def authenticate(self, username, password):
        return self.username == username and password == self.password


class AuthenticatedUser(Authentication, User):
    pass

assert issubclass(AuthenticatedUser, User) is True
assert issubclass(AuthenticatedUser, Authentication) is True

user1 = AuthenticatedUser('user1', 'password1')
assert user1.get_info() == 'Имя пользователя: user1'
assert user1.authenticate('user1', 'password2') is False
assert user1.authenticate('user1', 'password1') is True


# task2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f'Person {self.name}, {self.age}')


class Company:
    def __init__(self, company_name, location):
        self.company_name = company_name
        self.location = location

    def display_company_info(self):
        print(f'Company: {self.company_name}, {self.location}')


class Employee(Person, Company):
    def __init__(self, name, age, company_name, location):
        super().__init__(name, age)
        Company.__init__(self, company_name, location)

emp = Employee('Jessica', 28, 'Google', 'Atlanta')
emp.display_person_info()
emp.display_company_info()



