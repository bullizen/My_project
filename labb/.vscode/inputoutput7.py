handtag = open('.vscode/inputoutputfil.txt', 'r', encoding="utf-8")

# Läser in hela filen i en lista med rader
innehall = handtag.readlines()

print(innehall)
print(type(innehall))

# Stäng den öppnade filen
handtag.close()