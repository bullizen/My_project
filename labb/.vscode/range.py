for i in range(5):
    print(type(i), i)

# Konvertera till lista för att se innehållet bättre
print(list(range(5, 10)))

# Med tre argument: start, slut stopp
print(list(range(0, 10, 3)))

# Gå mot ett lägre värde, negativt hopp
print(list(range(10, 10, -3)))

# Total summa av 0 + 1 + 2 + 3
tot = sum(range(4))