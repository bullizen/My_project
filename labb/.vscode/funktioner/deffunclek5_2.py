anrop = 0


def minfunktion(x):
    global anrop
    anrop += 1
    print(x)


print("anrop", anrop)
minfunktion("Hej")
print("anrop", anrop)
minfunktion("Hopp")
print("anrop", anrop)
