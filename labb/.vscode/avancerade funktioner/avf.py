# Morgonövning
filmer = ("Filmer", ["Kindergarden Cop", "The Borrower"])
todo = ("Todo", ["Städa", "Mata katten", "Ring 1177"])
brod = ("Bröd", ["Limpa", "Knäckebröd", "Fullkorn"])

listor = [filmer, todo, brod]

index = 0

while True:
    lista = listor[index]
    print("Lista: " + lista[0])
    print("Val:")
    print("1 - Lägg till en ny rad i listan")
    print("2 - Skriv ut alla rader i listan med titeln först")
    print("3 - Gå till nästa lista")
    print("a - Avsluta")
    val = input("Ange val: ")

    if val == "a":
        break
    elif val == "3":
        # (0 + 1) % 3  -->  1
        # (1 + 1) % 3  -->  2
        # (2 + 1) % 3  -->  0
        # Darfor
        index = (index + 1) % len(listor)

        # Annat satt utan modulo
        # if index == len(listor) - 1:
        #     index = 0
        # else:
        #     index += 1
