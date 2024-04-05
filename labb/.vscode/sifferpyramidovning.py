siffror = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for sifferpyramid in siffror:
    w = str(sifferpyramid)
    print(w * sifferpyramid)

# Sifferpyramid
# Uppgiftsbeskrivning: Skapa ett mönster med siffror

# Målet med denna uppgift är att öva på att använda loopar i Python för att skriva ut ett specifikt mönster av siffror till konsolen.

# Uppgift:
# Din uppgift är att skriva en Python-skript som använder loopar för att skapa och skriva ut följande mönster:

# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

# Varje rad i mönstret består av siffran motsvarande radnumret upprepat så många gånger som radnumret.

# Tips:
# - Du kan använda strängmultiplikation för att upprepa siffrorna. Till exempel, `'5' * 5` ger `'55555'`.
# - Kom ihåg att loopvariabeln i en for-loop kan användas både för att bestämma vilken siffra som ska skrivas ut och hur många gånger den ska upprepas.
# Krav:

# - Ditt skript ska korrekt skriva ut det angivna mönstret till konsolen.
# - Du ska använda en for-loop för att genomföra uppgiften.