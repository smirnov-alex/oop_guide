# Практика "Создание класса и его методов"
'''
# task1
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f'{self.name} says {sound}'


# task2
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)



# task3
class Stack:
    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if self.is_empty():
            print('Empty Stack')
        else:
            return self.values.pop()

    def peek(self):
        if self.is_empty():
            print('Empty Stack')
            return None
        else:
            return self.values[-1]

    def is_empty(self):
        if len(self.values) > 0:
            return False
        else:
            return True

    def size(self):
        return len(self.values)



# task4
class Worker:
    def __init__(self, name, salary, gender, passport):
        self.name = name
        self.salary = salary
        self.gender = gender
        self.passport = passport

    def get_info(self):
        print(f'Worker {self.name}; passport-{self.passport}')

persons = [
    ('Allison Hill', 334053, 'M', '1635644202'),
    ('Megan Mcclain', 191161, 'F', '2101101595'),
    ('Brandon Hall', 731262, 'M', '6054749119'),
    ('Michelle Miles', 539898, 'M', '1355368461'),
    ('Donald Booth', 895667, 'M', '7736670978'),
    ('Gina Moore', 900581, 'F', '7018476624'),
    ('James Howard', 460663, 'F', '5461900982'),
    ('Monica Herrera', 496922, 'M', '2955495768'),
    ('Sandra Montgomery', 479201, 'M', '5111859731'),
    ('Amber Perez', 403445, 'M', '0602870126')
]
worker_objects = []
for item in persons:
    worker = Worker(item[0], item[1], item[2], item[3])
    worker_objects.append(worker)
for worker in worker_objects:
    worker.get_info()



# task5
class CustomLabel:

    def __init__(self, text, **kwargs):
        self.text = text
        for key, value in kwargs.items():
            setattr(self, key, value)

    def config(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


label = CustomLabel(text="Hello", bd=20, bg='#ffaaaa')
print(label.__dict__) # {'text': 'Hello', 'bd': 20, 'bg': '#ffaaaa'}
label.config(color='red', bd=100)
print(label.__dict__) # {'text': 'Hello', 'bd': 100, 'bg': '#ffaaaa', 'color': 'red'}



# task6
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Person: {self.name}, {self.age}")


class Company:
    def __init__(self, name, location):
        self.company_name = name
        self.location = location

    def display_company_info(self):
        print(f"Company: {self.company_name}, {self.location}")


class Employee:
    def __init__(self, name, age, company_name, city):
        self.personal_data = Person(name, age)
        self.work = Company(company_name, city)

emp = Employee('Jessica', 28, 'Google', 'Atlanta')
print(emp.personal_data.name)
print(emp.personal_data.age)
emp.personal_data.display_person_info()
print(emp.work.company_name)
print(emp.work.location)
emp.work.display_company_info()



# task7
class Task:
    def __init__(self, name, description, status=False):
        self.name = name
        self.description = description
        self.status = status

    def display(self):
        if self.status:
            state = 'Сделана'
        else:
            state = 'Не сделана'
        print(f'{self.name} ({state})')


class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)


class TaskManager:
    def __init__(self, task_list):
        self.task_list = task_list

    def mark_done(self, task):
        task.status = True

    def mark_undone(self, task):
        task.status = False

    def show_tasks(self):
        for item in self.task_list.tasks:
            item.display()
'''


# task2_4_1
class WeatherStation:
    __shared_attr = {
        'temperature': 0,
        'humidity': 0,
        'pressure': 0
    }

    def __init__(self):
        self.__dict__ = WeatherStation.__shared_attr

    def update_data(self, t, h, p):
        self.__shared_attr['temperature'] = t
        self.__shared_attr['humidity'] = h
        self.__shared_attr['pressure'] = p

    def get_current_data(self):
        return (self.__shared_attr['temperature'], self.__shared_attr['humidity'], self.__shared_attr['pressure'],)
