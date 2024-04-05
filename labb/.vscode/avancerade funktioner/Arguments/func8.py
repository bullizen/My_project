# ingen hjalp for ham, den ar av typen Any
def f(ham, eggs: str = "eggs") -> str:
    return ham.upper() + " and " + eggs


def f2(ham: str, eggs: str = "eggs") -> str:
    return ham.upper() + " and " + eggs


# ham ar antingen en int eller en float
def f3(ham: int | float, eggs: str = "eggs") -> str:
    return ham.upper() + " and " + eggs


print(f("hej"))
