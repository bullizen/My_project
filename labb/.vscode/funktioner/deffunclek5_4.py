def yttre(x):
    def inre(y):
        print("inre", y)

    inre(x)
    print("yttre", x)


# inre()  # NameError: name 'inre' is not defined

yttre(10)
