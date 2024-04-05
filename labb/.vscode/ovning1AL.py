# Skriv ut orden i en lista
# Uppgiftsbeskrivning: Iterera genom en lista med en while-loop

# Målet med denna uppgift är att öva på att använda while-loopen för att iterera genom elementen i en lista och skriva ut varje element till konsolen.

# Uppgift:
# Du har fått en lista med strängar:

lst = ["aaa", "bb", "eee", "ggg"]

index = 0
lst_length = len(lst)

while index < lst_length:
    print(lst[index])
    index += 1

# Din uppgift är att skriva ett Python-skript som använder en while-loop för att gå igenom varje position i listan och skriva ut varje ord med hjälp av `print()`-funktionen.

# Instruktioner:
# 1. Skapa en variabel som håller reda på din nuvarande position i listan (t.ex. index = 0).
# 2. Använd en while-loop som fortsätter så länge din position är mindre än längden på listan.
# 3. Inuti loopen, använd `print()` för att skriva ut elementet på den nuvarande positionen.
# 4. Öka din position med 1 efter varje iteration för att gå vidare till nästa element i listan.

# Krav:
# - Din skript ska korrekt skriva ut alla ord i listan till konsolen, ett ord per rad.
# - Du ska använda en while-loop för att genomföra iterationen.