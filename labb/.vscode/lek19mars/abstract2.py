from abc import ABC, abstractmethod
import math


class GeoObject(ABC):
    @abstractmethod
    def area():
        pass


class Rektangel(GeoObject):
    def __init__(self, bredd, hojd) -> None:
        super().__init__()

        self._bredd = bredd
        self._hojd = hojd

    def area(self):
        return self._bredd * self._hojd


class Cirkel(GeoObject):
    def __init__(self, radie) -> None:
        super().__init__()

        self._radie = radie

    def area(self):
        return self._radie**2 * math.pi


def print_area(o):
    if issubclass(o.__class__, GeoObject):
        print(o.area())


r = Rektangel(1000, 10)
c = Cirkel(400)

print_area(r)
print_area(c)
