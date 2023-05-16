# пространство имен класса


class DepartmentIT:
    PYTHON_DEV = 3
    GO_DEV = 3
    REACT_DEV = 2

    # нельзя напрямую обратиться к атрибутам из метода, ошибка NameError
    def info_error(self):
        print(PYTHON_DEV, GO_DEV, REACT_DEV)

    def info(self):
        print('via self:')
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    def info2(self):
        print('via classname:')
        print(DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV, DepartmentIT.REACT_DEV)

    @property
    def info_prop(self):
        print('via property:')
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    @classmethod
    def info_class(cls):
        print('via info_class:')
        print(cls.PYTHON_DEV, cls.GO_DEV, cls.REACT_DEV)

    @staticmethod
    def info_static():
        print('via info_static:')
        print(DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV, DepartmentIT.REACT_DEV)

    @staticmethod
    def make_backend():
        print('Python and Go')

    @staticmethod
    def make_frontend():
        print('React')

    def hiring_pyt_dev(self):
        self.PYTHON_DEV += 1

it1 = DepartmentIT()
# it1.info()
# it1.info2()
# it1.info_prop
# it1.info_class()
# it1.info_static()
print(it1.PYTHON_DEV)
it1.hiring_pyt_dev()
print(it1.PYTHON_DEV)
print(DepartmentIT.PYTHON_DEV)



