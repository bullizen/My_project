greetings = ["Hi", "Yo", "Greetings"]

index = 0


def greet(name):
    global index
    print(greetings[index], name)
    index = (index + 1) % len(greetings)


if __name__ == "__main__":
    print("greet name", __name__)

    greet("Xi")
    greet("Xi")
    greet("Xi")
    greet("Xi")
else:
    print("du importerar mig")
