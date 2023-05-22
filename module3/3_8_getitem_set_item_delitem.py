# Магические методы
# __getitem__, __setitem__, __delitem__


class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):
        if 1 <= item <= len(self.values):
            return self.values[item-1]
        else:
            raise IndexError('Индекс за границами коллекции')

    def __setitem__(self, key, value):
        if 1 <= key <= len(self.values):
            self.values[key-1] = value
        elif key > len(self.values):
            diff = key - len(self.values)
            self.values.extend([0]*diff)
            self.values[key-1] = value
        else:
            raise IndexError('Индекс за границами коллекции')

    def __delitem__(self, key):
        if 0 <= key < len(self.values):
            del self.values[key]
        else:
            raise IndexError('Индекс за границами коллекции')

# v1 = Vector(1, 2, 45, 567)
# v2 = Vector(3, 45, 34, 98, 87, 76)
# print(v1)
# print(v2[2])
# # print(v2[20])
# print(v2)
# v2[2] = 999
# print(v2)
# print(v2[2])
# del v2[2]
# print(v2)
# # del v2[6]
# v1[10] = 100
# print(v1)


# task1
class Building:
    def __init__(self, num):
        self.description = []
        self.description.extend([0]*num)

    def __getitem__(self, item):
        if 0 <= item < len(self.description):
            return self.description[item]
        else:
            raise IndexError('Индекс за границами коллекции')

    def __setitem__(self, key, value):
        if 0 <= key < len(self.description):
            self.description[key] = value
        else:
            raise IndexError('Индекс за границами коллекции')

    def __delitem__(self, key):
        if 0 <= key < len(self.description):
            del self.description[key]
        else:
            raise IndexError('Индекс за границами коллекции')


iron_building = Building(22)  # Создаем здание с 22 этажами
print(iron_building.description)
iron_building[0] = 'Reception'
iron_building[1] = 'Oscorp Industries'
iron_building[2] = 'Stark Industries'
print(iron_building[2])
del iron_building[2]
print(iron_building[2])
print(len(iron_building.description))


class MyDict:
    def __init__(self, **kwargs):
        self._data = kwargs

    def __str__(self):
        return str(self._data)

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value


my_dict = MyDict(a=1, b=2, c=3)
# print(my_dict['a'])
my_dict['d'] = 4
# print(my_dict)


# task2
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist


class Playlist:
    def __init__(self):
        self.songs = []

    def __getitem__(self, item):
        if 0 <= item < len(self.songs):
            return self.songs[item]
        else:
            raise IndexError('Индекс за границами коллекции')

    def __setitem__(self, key, value):
        if 0 <= key < len(self.songs):
            return self.songs.insert(key, value)

    def add_song(self, song):
        if isinstance(song, Song):
            self.songs.append(song)

playlist = Playlist()
assert len(playlist.songs) == 0
assert isinstance(playlist, Playlist)
playlist.add_song(Song("Paradise", "Coldplay"))
assert playlist[0].title == 'Paradise'
assert playlist[0].artist == 'Coldplay'
assert len(playlist.songs) == 1

playlist[0] = Song("Resistance", "Muse")
assert playlist[0].title == 'Resistance'
assert playlist[0].artist == 'Muse'
assert playlist[1].title == 'Paradise'
assert playlist[1].artist == 'Coldplay'

playlist[1] = Song("Helena", "My Chemical Romance")
assert playlist[1].title == 'Helena'
assert playlist[1].artist == 'My Chemical Romance'

assert playlist[2].title == 'Paradise'
assert playlist[2].artist == 'Coldplay'
print('Good')


# task3
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def __getitem__(self, item):
        if item in self.items.keys():
            return self.items[item]
        else:
            return 0

    def __setitem__(self, key, value):
        self.items[key] = value

    def __delitem__(self, key):
        if key in self.items.keys():
            del self.items[key]
        else:
            raise IndexError('Индекс за границами коллекции')

    def add_item(self, item, value=1):
        self.items[item] = self.items.get(item, 0) + value

    def remove_item(self, item, value=1):
        if item not in self.items.keys():
            pass
        elif self.items[item] <= value:
            self.__delitem__(item)
        else:
            self.items[item] = self.items[item] - value

# Create a new shopping cart
cart = ShoppingCart()

# Add some items to the cart
cart.add_item('Apple', 3)
cart.add_item('Banana', 2)
cart.add_item('Orange')

assert cart['Banana'] == 2
assert cart['Orange'] == 1
assert cart['Kivi'] == 0

cart.add_item('Orange', 9)
assert cart['Orange'] == 10

print("Shopping Cart:")
for item_name in cart.items:
    print(f"{item_name}: {cart[item_name]}")

cart['Apple'] = 5
cart['Banana'] = 7
cart['Kivi'] = 11
assert cart['Apple'] == 5
assert cart['Banana'] == 7
assert cart['Kivi'] == 11

print("Updated Shopping Cart:")
for item_name in cart.items:
    print(f"{item_name}: {cart[item_name]}")

# Remove an item from the cart
cart.remove_item('Banana')
assert cart['Banana'] == 6

cart.remove_item('Apple', 4)
assert cart['Apple'] == 1

cart.remove_item('Apple', 2)
assert cart['Apple'] == 0
assert 'Apple' not in cart.items

cart.remove_item('Potato')

del cart['Banana']
assert cart['Banana'] == 0
assert 'Banana' not in cart.items

print("Updated Shopping Cart:")
for item_name in cart.items:
    print(f"{item_name}: {cart[item_name]}")