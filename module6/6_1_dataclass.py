from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    balance: int


jack = Customer('jack', 500)
print(jack)
print(jack.name, jack.balance)


# task1
@dataclass
class Point:
    x: int
    y: int

point1 = Point(5, 7)
point2 = Point(-10, 12)
print(point1)
print(point2)


@dataclass
class InventoryItem:
    name: str
    price: float = 9.99
    quantity: int = 1


desk = InventoryItem('Computer desk', 1000, 12)
pen = InventoryItem('Pen')
monitor = InventoryItem('Monitor', 300)
clock = InventoryItem('Clock', quantity=10)
print(desk)
print(pen)
print(monitor)
print(clock)


# task2
@dataclass
class Location:
    name: str
    longitude: float = 0
    latitude: float = 11.5

stonehenge = Location('Stonehenge', longitude=51, latitude=1.5)
print(stonehenge)


