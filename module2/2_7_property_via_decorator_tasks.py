'''
class Notebook:
    def __init__(self, notes) -> None:
        self._notes = notes
    
    @property
    def notes_list(self):
        for i in range(1, len(self._notes) + 1):
            print(f'{i}.{self._notes[i-1]}')

note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
note.notes_list
'''

class Money:
    def __init__(self, dollars, cents) -> None:
        self.total_cents = dollars*100 + cents

    @property
    def dollars(self):
        return self.total_cents//100
    
    @dollars.setter
    def dollars(self, value):
        if (not isinstance(value, int)) or value < 0:
            print(f'Error dollars')
        else:
            self.total_cents=value*100 + self.cents

    @property
    def cents(self):
        return self.total_cents%100
    
    @cents.setter
    def cents(self, value):
        if (not isinstance(value, int)) or value < 0 or value >= 100:
            print(f'Error cents')
        else:
            self.total_cents=self.dollars * 100 + value

    def __str__(self) -> str:
        return(f'Ваше состояние составляет {self.dollars} долларов {self.cents} центов')

Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
print(Bill.total_cents) # 10199
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов
print(Bill.total_cents) # 66612