# Менеджер контекста


class CustomManagerContext:
    def __enter__(self):
        print('Start manager context')
        return [1, 2, 3]

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('End manager context')
        print(exc_type, exc_val, exc_tb, sep=', ')
        if isinstance(exc_val, ZeroDivisionError):
            print('Нельзя делить на ноль')
            return True
        # return True


class FileContext:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        print('Open file')
        self.file = open(self.path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Close file')
        self.file.close()



# with open('passwords.txt', 'w') as file:
#     file.write('hello')

# with CustomManagerContext() as cust:
#     print('hello')
#     print(cust)
#     1/0
#     12 + 'dgfdf'
#
# print('Finally end')

# with FileContext('passwords.txt', 'r') as file:
#     print(file.read())

class MyContextManager:
    def __enter__(self):
        print("Entering context")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")


with MyContextManager():
    print("Inside context")


class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
            return self.file
        except FileNotFoundError:
            print("Error: File not found")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with FileManager("test.txt", "r") as f:
    if f:
        print(f.read())
        