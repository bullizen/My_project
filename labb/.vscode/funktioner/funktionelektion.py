# Global variabel för den är inne i en funktion
# Kan läsas inne i is_lenghty

max_len = 3

def is_lenghty(seq):
    length = len(seq)

    # Gör så att vi kan skriva över den globala 
    global max_len

    # Vi kan läsa den globala variabeln
    print(max_len)

    max_len = 2

    # if max_len < lenght:
    #     max_len = length

    result = len(seq) >10
    return result

x1 = is_lenghty("nackademin")
x2 = is_lenghty("skinnskatteberg")