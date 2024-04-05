a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]

b = [-1, 1, 66.25, 333, 333, 1234.5]
del b[3:5]  # bort 3 och 4

c1 = [-1, 1, 66.25, 333, 333, 1234.5]
# tar bort allt
del c1[:]

# tydligare
c2 = [-1, 1, 66.25, 333, 333, 1234.5]
c2.clear()

hej = "Hej"
# tar bort variabeln
del hej
