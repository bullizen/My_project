def calculate(first=0, *numbers, operator="+"):
    result = first
    for number in numbers:
        if operator == "+":
            result = result + number
        else:
            result = result - number

    # Minusfall:
    # 10, 1, 2  -> 10 - 1 - 2    = 7
    # 5, 5      -> 5 - 5         = 0
    # <inget>   -> inget - inget = 0

    return result


# print(calculate(1, 2, 3, 4))  # Förväntat returvärde: 10
# print(calculate(1, 2, 3, 4, operator="+"))  # Förväntat returvärde: 10
print(calculate(10, 1, 2, operator="-"))  # Förväntat returvärde: 7
print(calculate(5, 5, operator="-"))  # Förväntat returvärde: 0
print(calculate())  # Förväntat returvärde: 0 (inga argument)

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 20)
    print("keywords type", type(keywords))
    for kw in keywords:
        print(kw, ":", keywords[kw])


Peter = "Hare"
cheeseshop("Herrgard", "Pos1", Peter, vilketordjagvill="Hushallssak")
