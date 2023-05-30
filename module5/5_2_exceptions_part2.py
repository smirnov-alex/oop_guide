# распространение исключений

def first():
    print('start first')
    try:
        second()
    except ZeroDivisionError:
        print ('handling first')
    print('finish first')

def second():
    print('start second')
    third()
    print('finish second')

def third():
    print('start third')
    1/0
    print('finish third')

print('hello')
first()

def function_1():
    print('Start')
    1/0
    print('End')


def function_2():
    try:
        function_1()
    except ZeroDivisionError:
        print("Отловили ZeroDivisionError")


function_2()
