from enum import Enum

Color = Enum('Color', ['RED', 'GREEN', 'BLUE'])

favorit = Color.RED

print(type(favorit), favorit.value, favorit.name)