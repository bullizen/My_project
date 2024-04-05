listadisney = ["Cinderella", "Aladdin", "Frozen", "Lionking", "Beauty and the Beast"]

index = 0
while index < len(listadisney):
    film = listadisney[index]
    index += 1
    while 'e' in film:
        print(film)
        break
    else:
        print("Disneyfilmer är bäst!")
    if not 'e':
        print("Inga Disneyfilmer med bokstaven 'e' i namnet hittades")
    