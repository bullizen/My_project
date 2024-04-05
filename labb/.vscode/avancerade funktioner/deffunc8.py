# {}  dict
# []  list
# ()  tuple

#           .
#    gren1 / \ gren2
#    ugren1  /\ ugren2
#   ugren1  /\ ugren2

ugren1_varde = {"ugren3": 55, "ugren4": "hejsan"}
gren2_varde = {"ugren1": ugren1_varde, "ugren2": "hej"}
trad = {"gren1": "k", "gren2": gren2_varde}


def berakna_djup(trad: dict, djup=0):
    djup = djup + 1
    # unpacking
    for value in trad.values():
        if isinstance(value, dict):
            ret_djup = berakna_djup(value, djup)
            if ret_djup > djup:
                djup = ret_djup

    return djup


djup = berakna_djup(trad)

print("djuper ar", djup)
