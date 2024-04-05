def treecoords(tree: dict, current_coord: tuple = ()) -> tuple:
    coordinates = []

    for key, value in tree.items():
        print(f"Key: {key}, Value: {value}")
        if isinstance(value, dict):
            sub_coordinates = treecoords(value, current_coord + (key,))
            coordinates.extend(sub_coordinates)
        else:
            coordinates.append((current_coord + (key,), value))

    return coordinates


# Test med frukter och deras godhet på skala 0-10 samt deras namn på latin.
tree = {
    "Äpple": {"Godhet": 7, "Latin": "Malus domestica"},
    "Banan": {"Godhet": 9, "Latin": "Musa"},
    "Apelsin": {"Godhet": 6, "Latin": "Aurantiacus"},
    "Kiwi": {"Godhet": 7, "Latin": "Actinidia deliciosa"},
    "Mango": {"Godhet": 10, "Latin": "Mangifera indica"},
}

# Resultatet från funktionen "treecords" tilldelas variabel "result" med "tree" som argument.
# Printa sedan resultatet som förväntas vara en tuple med koordinaterna och värderna i varje element i "tree".
result = treecoords(tree)
print(result)

tree["Päron"] = {"Godhet": 6, "Latin": "Pyrus"}
tree["Äpple"]["Godhet"] = 6
tree["Orange frukt"] = tree.pop("Apelsin")