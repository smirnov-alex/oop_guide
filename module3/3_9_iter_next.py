# магические методы
# методы __iter__, __next__

'''
class Mark:
    def __init__(self, values):
        self.values = values
        self.index = 0

    def __iter__(self):
        print('call __iter__ for marks')
        return self

    def __next__(self):
        print('call next marks')
        if self.index >= len(self.values):
            self.index = 0
            raise StopIteration
        letter = self.values[self.index]
        self.index += 1
        return letter


class Student:

    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    # если есть метод __getitem__, то Python использует его для обхода в цикле for
    def __getitem__(self, item):
        return self.name[item]

    # если определен метод __iter, то Python использует его для обхода в цикле for
    def __iter__(self):
        print('call __iter__')
        self.index =0
        # return iter(self.marks)
        return self

    def __next__(self):
        print('call next students')
        if self.index >= len(self.name):
            raise StopIteration
        letter = self.name[self.index]
        self.index += 1
        return letter

m = Mark([3, 4, 5, 5, 5, 4, 3])
igor = Student('Igor', 'Nikolaev', m)
for i in igor:
    print(i)


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} {self.suit}'


class Deck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __getitem__(self, item):
        return self.cards[item]


deck = Deck()
for card in deck:
    print(card)



class FileReader:
    def __init__(self, filename):
        self.file = open(filename)

    def __iter__(self):
        return self

    def __next__(self):
        return self.file.__next__().strip()

for line in FileReader('lorem.txt'):
    print(line)
'''


class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < 0:
            raise StopIteration
        letter = self.start
        self.start -= 1
        return letter


# print('Элементы итератора Countdown(7)')
# for i in Countdown(7):
#     print(i)
#
# print('-' * 10)
# print('Элементы итератора Countdown(10)')
# for i in Countdown(10):
#     print(i)

class PowerTwo:
    def __init__(self, step):
        self.step = step

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index > self.step:
            raise StopIteration
        result = 2 ** self.index
        self.index += 1
        return result


numbers = PowerTwo(2)

assert hasattr(numbers, '__next__') is True
assert hasattr(numbers, '__iter__') is True

iterator = iter(numbers)
print('Элементы итератора PowerTwo(2)')
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
    print(next(iterator))
    raise ValueError('Не реализовали StopIteration')
except StopIteration:
    pass


class InfinityIterator:
    def __init__(self):
        self.step = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.step
        self.step += 10
        return result
