# расширение Extending
# создание метода, которого нет в родительском классе

class Person:
    age = 25
    def breathe(self):
        print('Человек дышит')

    def sleep(self):
        print("Человек спит")

    def combo(self):
        self.breathe()
        if hasattr(self, 'walk'):
            self.walk()
        self.sleep()
        if hasattr(self, 'age'):
            print(self.age)


class Doctor(Person):

    age = 30

    def sleep(self):
        print("Доктор спит")

    def breathe(self):
        print('Доктор дышит')

    def walk(self):
        print('Доктор идет')

p = Person()
d = Doctor()
# d.sleep()
# p.breathe()
# d.breathe()
p.combo()
print('-' * 20)
d.combo()
