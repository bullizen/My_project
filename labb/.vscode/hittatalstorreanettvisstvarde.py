# # Hitta Tal Större än ett Visst Värde

# # I denna uppgift ska du skapa en funktion med namnet find_greater_than som tar en lista av tal och ett specifikt värde som input. Funktionens uppgift är att returnera en ny lista som endast innehåller de tal från den ursprungliga listan som är större än det angivna värdet.

# # Funktionsspecifikation:

# # - Funktionsnamn: find_greater_than
# # - Argument:
# #   - lista (list): En lista av heltal eller flyttal.
# #   - varde (int eller float): Ett heltal eller flyttal som funktionen ska jämföra listelementen med.
# # - Returvärde: Funktionen ska returnera en lista med de tal från den ursprungliga listan som är större än det angivna värdet.

# # Exempel:

# # 1. Exempel 1:

# #    - Input: find_greater_than([-3, 2, 8, 15, 31, 5, 4, 8], 5)
# #    - Förväntat resultat: [8, 15, 31, 8]
# #    - Förklaring: Endast talen som är större än 5 från den ursprungliga listan inkluderas i den returnerade listan.

# # Instruktioner:

# # 1. Definiera funktionen find_greater_than med de angivna argumenten.
# # 2. Använd en loop eller list comprehension för att iterera genom den givna listan och välj ut de tal som är större än det angivna värdet.
# # 3. Returnera den nya listan som innehåller endast de utvalda talen.

# # Tips:

# # - Använd list comprehension för en mer kompakt och läsbar kod.
# # - Kom ihåg att testa din funktion med olika listor och värden för att säkerställa att den fungerar korrekt.

# # Lycka till med att skapa din funktion som hittar och returnerar tal större än ett specifikt värde!

# # Listhanterare


# # Om vi börjar med datastrukturen:

# # filmer = ("Filmer", ["Kindergarden Cop", "The Borrower"])
# # todo = ("Todo", ["Städa", "Mata katten", "Ring 1177"])
# # brod = ("Bröd", ["Limpa", "Knäckebröd","Fullkorn"])

# # listor = [filmer, todo, brod]

# # Skapa ett program som fungerar enligt nedanstående exempel:

# Lista: Filmer
# Val:
# 1 - Lägg till en ny rad i listan
# 2 - Skriv ut alla rader i listan med titeln först
# 3 - Gå till nästa lista
# a - Avsluta

# Ange val: 1
# Ange rad: James Bond

# Lista: Filmer
# Val:
# 1 - Lägg till en ny rad i listan
# 2 - Skriv ut alla rader i listan med titeln först
# 3 - Gå till nästa lista
# a - Avsluta

# Ange val: 2
# Filmer
# -----------
# Kindergarden Cop
# The Borrower
# James Bond

# Lista: Todo
# Val:
# 1 - Lägg till en ny rad i listan
# 2 - Skriv ut alla rader i listan med titeln först
# 3 - Gå till nästa lista
# a - Avsluta

# Ange val: 3

# <programmet avslutas>




# Tips:
# input() för att ta in inmatning från användaren
# break för att avbryta en oändlig while True-loop
# listindex = listindex + 1 % len(listor)
# inte ett måste, men kanske en "unpacking" någonstans är snyggt?
