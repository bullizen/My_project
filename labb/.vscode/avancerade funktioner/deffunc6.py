def hej(s):
    tillagg = input("Tillägg: ")

    beraknat = s + tillagg

    if len(tillagg) > 0:
        return hej(beraknat)

    return beraknat


# print(nr) # NameError: name 'nr' is not defined

ret = hej("hoppsan")

print(ret)
