class Cat:
    color = 'white'

    def hello(*args):
        print('Meow!', args)

    def show_color(self):
        print(f'my color is {self.color}')

    def show_name(self):
        if hasattr(self, 'name'):
            print(f'my name is {self.name}')
        else:
            print('Nothing')

    def set_value(self, value, age=0):
        self.name = value
        self.age = age


bob = Cat()
bob.hello()
bob.show_color()
bob.color = 'black'
bob.show_color()
bob.name = 'BOB'
bob.show_name()

tom = Cat()
tom.show_name()
tom.set_value('TOM', 6)
tom.show_name()
tom.name
print(tom.age)
