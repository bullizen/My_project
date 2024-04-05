def yttre(x):
    def inre():
        nonlocal x
        x = 999
        print("inre", x)

    inre()
    print("yttre", x)


# inre()  # NameError: name 'inre' is not defined

yttre(10)
