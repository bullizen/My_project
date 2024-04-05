lst1 = ["a", "b", "c"]
lst2 = [1, 2, 3]

zippat = list(zip(lst1, lst2))

lang_lista = lst1.copy()
lang_lista.extend(lst2)

print(zippat)
print(lst1)
print(lang_lista)
