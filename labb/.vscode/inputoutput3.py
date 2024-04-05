lista = [("ford", 2), ("volvo", 5), ("mustang", 99), ("mazda", 212)]

for modell, antal in lista:
    rad_strang = "{:8}|{:9}".format(modell, antal)
    print(rad_strang)