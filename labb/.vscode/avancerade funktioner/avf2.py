filmer = ("Filmer", ["Kindergarden Cop", "The Borrower"])
todo = ("Todo", ["Städa", "Mata katten", "Ring 1177"])
brod = ("Bröd", ["Limpa", "Knäckebröd", "Fullkorn"])

alla_listor = [filmer, todo, brod]

index = 0

while True:
    aktuell_lista = alla_listor[index]
    print("")
    print("Lista: " + aktuell_lista[0])
    print("Val:")
    print("1 - Lägg till en ny rad i listan")
    print("2 - Skriv ut alla rader i listan med titeln först")
    print("3 - Gå till nästa lista")
    print("a - Avsluta")
    print("")
    val = input("Ange val: ")
    print("")

    if val == "a":
        break
    elif val == "1":
        angiven_rad = input("Ange rad: ")
        aktuell_lista[1].append(angiven_rad)

        # nuvarande_rader = aktuell_lista[1]
        # nuvarande_rader.append(angiven_rad)
    elif val == "2":
        print(aktuell_lista[0])
        print("--------")
        aktuell_listas_rader = aktuell_lista[1]
        for angiven_rad in aktuell_listas_rader:
            print(angiven_rad)
    elif val == "3":
        index = (index + 1) % len(alla_listor)  # 3 % 3  -> 0
