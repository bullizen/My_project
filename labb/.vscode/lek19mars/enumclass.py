from enum import Enum

# class syntax
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

favorit = Color.RED
print(type(favorit), favorit.value, favorit.name)