def multi_greet(*alla_namn, greeting="hej"):
    for namn in alla_namn:
        print(greeting + " " + namn)


multi_greet("Kent", "Ulla", "Xi", "Bo", greeting="Yo")


def multi_greet2(greeting, *alla_namn):
    for namn in alla_namn:
        print(greeting + " " + namn)


multi_greet("Hej", "Kent", "Ulla", "Xi", "Bo")
