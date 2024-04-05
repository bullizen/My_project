listadisney = ["cinderella", "aladdin", "frozen", "lionking", "beauty and the beast"]

listadisney2 = ["cINDERELLA", "aLADDIN", "fROZEN", "lIONKING", "bEAUTY AND THE BEAST"]

listadisney3 = ["   cinderella", "aladdin", "  frozen", " lionking", "    beauty and the beast"] 

versaler = [film.upper() for film in listadisney]

first = [film.capitalize() for film in listadisney]

swap = [film.swapcase() for film in listadisney2]

strip = [film.strip() for film in listadisney3]

print(versaler)
print(first)
print(swap)
print(strip)

