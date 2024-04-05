# palindromish funktion som kan ta emot 2 värden från en lista
def palindromish(ord=None, grad=None):

    # kontrollerar om grad är inget eller mindre eller lika med noll
    if ord == None or len(ord) < 1:
        print(
            "Antal bostäver = ",
            len(ord),
            " En tom sträng får anses vara det kortaste palindromet\n",
        )
        return True
        # kontrollerar ordet om graden inte är angiven
    elif grad == None or grad > len(ord) // 2:

        langd = len(ord)
        langddelat = langd // 2
        vanster = ord[:langddelat]
        hoger = ord[-langddelat:]
        if vanster == hoger[::-1]:

            print(
                vanster,
                " är lika med ",
                hoger[::-1],
                ", är ett palindrom, räknat på grad \n",
                langddelat,
            )
            return True
        else:
            print(
                vanster,
                " är inte lika med ",
                hoger[::-1],
                ", inget palindrom, räknat på grad \n",
                langddelat,
            )
            return False

    # kontrollerar om grad är skiljt från inget och om det är större än noll
    elif grad != None:
        vanster = ord[:grad]
        hoger = ord[-grad:]
        if vanster == hoger[::-1]:
            print(vanster, ", är lika med,", hoger[::-1], ", ordet är en palindrom\n")
            return True
        else:
            print(
                vanster,
                "och",
                hoger[::-1],
                ", är ej lika med varandra ordet är ej en palindrom\n",
            )
            return False


if __name__ == "__main__":
    palindromish(
        "mamma",
    )
    palindromish("radar", 2)
    palindromish("")
    palindromish("example", 3)
    palindromish([1, 2, 3, 50, 60, 3, 2, 1], 3)
    palindromish([1, 2, 3, 50, 60, 3, 2, 1], 4)