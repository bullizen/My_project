# Fore bild
class SifferOperation:
    def __init__(self, num) -> None:
        self._num = num

    def dubbla(self):
        self._num = self._num * 2

    def dela(self, namnaren):
        self._num = self._num // namnaren

    def gangra(self, tal):
        self._num = self._num * tal

    def print(self):
        print(self._num)

    def __str__(self):
        return str(self._num)

s = SifferOperation(2)

# Fluent API -> Returnera self
s.dubbla()
s.dubbla()
s.dubbla()
s.print()
s.dela(2)
s.print()
s.gangra()



print(s)