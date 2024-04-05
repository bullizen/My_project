# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#       -----------    ----------     ----------
#         |             |                  |
#         |        Positional or keyword   |
#         |                                - Keyword only
#          -- Positional only


def f2(a, b, *, c):
    print(a + b)


# fel
# f2(1, 2, 3)
# ratt
f2(1, 2, c=3)


def f1(a, b, /):
    print(a + b)


# fel
# f1(1, b=2)
# ratt
# f1(1, 2)
