# вычисляемые property
'''
class Rectangle:
    def __init__(self, h, w):
        self.height = h
        self.width = w
        self.__area = None

    @property
    def area(self):
        self.__area = self.width * self.height
        return self.__area

r1 = Rectangle(5, 10)
assert isinstance(r1, Rectangle)
assert r1.area == 50
assert isinstance(type(r1).area, property), 'Вы не создали property area'

r2 = Rectangle(15, 3)
assert isinstance(r2, Rectangle)
assert r2.area == 45
assert isinstance(type(r2).area, property), 'Вы не создали property area'

r3 = Rectangle(43, 232)
assert r3.area == 9976
print('Good')




# task2
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @property
    def date(self):
        return f'{self.day:02}/{self.month:02}/{self.year:04}'

    @property
    def usa_date(self):
        return f'{self.month:02}-{self.day:02}-{self.year:04}'

d1 = Date(5, 10, 2001)
assert isinstance(d1, Date)
print(d1.date, d1.usa_date)
assert d1.date == '05/10/2001'
assert d1.usa_date == '10-05-2001'
assert isinstance(type(d1).date, property), 'Вы не создали property date'
print(d1.date, d1.usa_date)

d2 = Date(15, 3, 999)
print(d2.date, d2.usa_date)
assert isinstance(d2, Date)
assert d2.date == '15/03/0999'
assert d2.usa_date == '03-15-0999'
assert isinstance(type(d2).date, property), 'Вы не создали property date'
print(d2.date, d2.usa_date)

d3 = Date(3, 5, 3)
assert d3.date == '03/05/0003'
assert d3.usa_date == '05-03-0003'
print(d3.date, d3.usa_date)
'''


# task3
class Password:
    def __init__(self, password):
        self.password = password

    @property
    def strength(self):
        if len(self.password) < 8:
            return 'Weak'
        elif len(self.password) >= 12:
            return 'Strong'
        else:
            return 'Medium'

pass_1 = Password("Alligator34")
assert pass_1.password == "Alligator34"
assert pass_1.strength == "Medium"
assert len(pass_1.__dict__) == 1, 'У ЭК должен храниться только один атрибут'
print(pass_1.__dict__)

pass_2 = Password("Alligator345678")
assert pass_2.password == "Alligator345678"
assert pass_2.strength == "Strong"
pass_1.password = "123"
assert pass_1.strength == "Weak"
assert len(pass_2.__dict__) == 1, 'У ЭК должен храниться только один атрибут'

pass_3 = Password("345678")
assert pass_3.strength == "Weak"
print('Good')
assert len(pass_3.__dict__) == 1, 'У ЭК должен храниться только один атрибут'