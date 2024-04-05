x = 10
y = 1337


def minfunktion():

    # andras bara inne i funktonen, nu kan vi inte lasa
    # x fran det globala langre.
    x = 99
    print("Hej fran min funktion ar x", x)
    global y
    y = 2024
    print("Hej fran min funktion ar y", y)


minfunktion()
print("Utanfor funktionen ar x", x)
print("Utanfor funktionen ar y", y)
