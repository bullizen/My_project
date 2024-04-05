squares = [1, 4, 9, 16, 25]

# sist = squares[-1]

# nylista = squares[1:4]

# nylista2 = squares[-2:]

# lista3 = squares[:]

print(id(squares))

lista3 = squares
lista4 = squares[1:]

lista3.append(999)

del lista4[3]

print(id(lista3))
print(id(lista4))

str2 = "hej" + "san"
