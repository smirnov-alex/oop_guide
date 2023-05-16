class Cat:

    def __init__(self, name, breed='pers', age=1, color='white'):
        print('hello, new object is', self, name, breed, age, color)
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color


tom = Cat('Tom')
kelly = Cat('Kelly', age=3)
