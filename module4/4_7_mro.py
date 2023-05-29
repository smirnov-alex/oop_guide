# Аббревиатура MRO – method resolution order (переводится как «порядок разрешения методов»).
# Этот порядок относится не только к поискам методов, но и к прочим атрибутам класса, так как методы –
# это частный случай более общего понятия «атрибут».


class A:
    def hello(self):
        print('hello from A')


class B:
    def hello(self):
        print('hello from B')


class C(A, B):
    def hello(self):
        print('hello from C')

C().hello()
