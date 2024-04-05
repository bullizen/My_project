class MyError(Exception):
    pass

def a():
    b()
    print"Slutet på a()"

def b():
    c()

def c():
    d()

def d():
    try:
        print(1 / 0)
    except ZeroDivisionError
        print("Ingen fara!")

a()