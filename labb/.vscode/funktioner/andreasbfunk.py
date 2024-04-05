def palindromish(word, grad=None):

# Anger grad automatiskt om värdet lämnas tomt.
    if grad == None:
        grad = len(word) // 2

    #Om graden är större än möjlig grad, så justeras graden till hösta möjliga.
    elif grad > len(word) // 2:
        grad = len(word) // 2

# Använder slicing för att få ut första och sista bokstäverna, baserad på graden
    reversed = word[::-1]
    firstletters = word[0:grad]
    lastletters = reversed[0:grad]


    # För att konvertera stränger till lower
    if isinstance(word, str) == True:
        firstletters = firstletters.lower()
        last_letters = last_letters.lower()
        reversed = reversed.lower()
        word = word.lower()

    # Kontrollerar först ifall ordet är en palindrom i sin helhet
    if word == reversed:
        print(f"[TRUE] - [{word}] är ett palindrom i sin helhet")
        return True

# Kontrollerar om ordet är en palindrom med hjälp av graden
    elif first_letters == last_letters:
        print(f"[TRUE] - [{word}] Är ett palindrom av graden [{grad}]")
        return True
    # Annars är det inte ett palindrom av den angivna graden.
    else:
        print(f"[FALSE] - [{word}] Är inte ett palindom av graden [{grad}]")
        return False


if '__name' == "__main":
    palindromish("radar", 2)
    palindromish([1, 2, 3, 50, 60, 3, 2, 1], 3)
    palindromish([1, 2, 3, 50, 60, 3, 2, 1], 4)
    palindromish("example", 3)
    palindromish("Naturrutan")
    palindromish("")
    palindromish("kajak", 1000)
    palindromish("solros", 2)
    palindromish("solros", 3)