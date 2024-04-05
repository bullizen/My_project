# Hitta Tal Större än ett Visst Värde

# I denna uppgift ska du skapa en funktion med namnet find_greater_than som tar en lista av tal och ett specifikt värde som input. Funktionens uppgift är att returnera en ny lista som endast innehåller de tal från den ursprungliga listan som är större än det angivna värdet.

# Funktionsspecifikation:

# - Funktionsnamn: find_greater_than
# - Argument:
#   - lista (list): En lista av heltal eller flyttal.
#   - varde (int eller float): Ett heltal eller flyttal som funktionen ska jämföra listelementen med.
# - Returvärde: Funktionen ska returnera en lista med de tal från den ursprungliga listan som är större än det angivna värdet.

# Exempel:

# 1. Exempel 1:

#    - Input: find_greater_than([-3, 2, 8, 15, 31, 5, 4, 8], 5)
#    - Förväntat resultat: [8, 15, 31, 8]
#    - Förklaring: Endast talen som är större än 5 från den ursprungliga listan inkluderas i den returnerade listan.

# Instruktioner:

# 1. Definiera funktionen find_greater_than med de angivna argumenten.
# def find_greater_then([-10, -5, 0, 1, 3, 6, 54, 88], 5):
#     if find_greater_then > 5:
#         return find_greater_then

def find_greater_then(in_lst, value):
    ut_lst = []
    for element in in_lst:
        if element > 5:
            ut_lst.append(element)
    return ut_lst

x = find_greater_then([-10, -5, 0, 1, 3, 5, 6, 54, 80], 5)

# append = lägg till på slutet



#for x in find_greater_then:
#     x = ((-10), (-5), (0,), (1), (3), (6), (54), (88))
#     print(x > 5)

# 2. Använd en loop eller list comprehension för att iterera genom den givna listan och välj ut de tal som är större än det angivna värdet.
# 3. Returnera den nya listan som innehåller endast de utvalda talen.

# Tips:

# - Använd list comprehension för en mer kompakt och läsbar kod.
# - Kom ihåg att testa din funktion med olika listor och värden för att säkerställa att den fungerar korrekt.

# Lycka till med att skapa din funktion som hittar och returnerar tal större än ett specifikt värde!


