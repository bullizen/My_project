def funktionsnamn(bar):
    print(bar)


def minandrafunktion(r):
    print(r + "!")


funktionsnamn("Min text")
minandrafunktion("Min text")

---
def funktionsnamn(bar):
    return bar + "!"


mitt_varde = funktionsnamn("Min text")

print(mitt_varde)


def funktionsfabrik(varde1):
    def leverans(varde2):
        return varde1 + varde2

    return leverans


leverans = funktionsfabrik(5)

print(type(leverans))

result = leverans(11)
