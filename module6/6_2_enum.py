from enum import Enum
from pprint import pprint


class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


pprint(list(Weekday))


class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4


print(Season.SPRING)
print(Season.SPRING.name)
print(Season.SPRING.value)
# Получаем доступ через значение. Обратите внимание, запись в круглых скобках
print("Элемент, который ассоцируется со значением 3 это ",
      Season(3).name)

# Доступ по ключу через имя атрибута
print("Значение элемента, кот-ый ассоцируется с именем WINTER",
      Season['WINTER'].value)

from enum import Enum


class Direction(Enum):
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"


print(Direction.WEST.name)
print(Direction.SOUTH.value)
