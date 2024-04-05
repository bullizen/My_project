# Hundår
# Uppgiftsbeskrivning: Beräkna en hunds ålder i hundår

# Målet med denna uppgift är att öva på att använda villkorssatser och matematiska operationer i Python för att konvertera hunds ålder från människoår till hundår.

# Uppgift:

# Skriv ett Python-program som beräknar en hunds ålder i hundår. Notera att under de första två åren räknas varje hundår som 10.5 människoår. Efter de första två åren motsvarar varje hundår 4 människoår.

# Hund 0 år = 0
# Människan 1 år = 10,5 Hundår
# Månniskan 2 år = 21 Hundår (därefter +4 människorår)
# Människan 3 år = 25 Hundår
# Människan 4 år = 29 Hundår

# Hund0 = [0]
# Människa0 = [0]

# Hund1 = [10.5]
# Människa1 = [1]

# Hund2 = [21]
# Människa2 = [2]

# Hund3 = [25]
# Människa3 [3]

# Hund4 = [29]
# Människa4 = [4]

# Hund5 = [33]
# Människa5 = [5]

# Hund6 = [36]
# Människa6 = [6]

människoår_sträng = input("Hundens år i människoår: ")
människoår = int(människoår_sträng)

if människoår < 2:
    hundår = människoår * 10.5
    print("Hundens ålder i hundår är:", hundår)
else:
    hundår = 21 + (människoår - 2) * 4
    print("Hundens ålder i hundår är:", hundår)



# Instruktioner:

# 1. Be användaren mata in en hunds ålder i människoår.
# 2. Använd en villkorssats för att avgöra hur åldern ska beräknas beroende på om hunden är yngre eller äldre än två år.
# 3. Beräkna hundens ålder i hundår baserat på de angivna reglerna.
# 4. Skriv ut hundens ålder i hundår med hjälp av print()-funktionen.

# Exempel på förväntad utdata:

# Input a dog's age in human years: 15
# The dog's age in dog's years is 73

# Tips:

# - Använd input() för att läsa in hundens ålder i människoår.
# - Använd en if-sats för att avgöra om hunden är yngre eller äldre än två år och beräkna sedan åldern enligt de angivna reglerna.
# - Kom ihåg att konvertera inmatningen från sträng till ett numeriskt värde för att kunna utföra beräkningar.

# Krav:

# - Programmet ska korrekt läsa in en ålder i människoår och konvertera den till hundår.
# - Korrekt användning av villkorssatser och matematiska operationer för att utföra beräkningen.

# Lycka till med att skriva programmet som beräknar en hunds ålder i hundår!
