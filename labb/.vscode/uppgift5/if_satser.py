listanamn = ["Julia", "Elisabeth", "Michaela"]

for element in listanamn:
    if len(element) == 4:
        print(element)
    elif len(element) > 10:
       print(element * 2)
    else:
        print("Hejsan hoppsan")
        break