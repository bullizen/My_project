namnlista = ["bo", "john", "eva", "[STOP]", "jonathan", "bosse"]

for element in namnlista:
    if len(element) < 4:
        continue

    print(element)
print("-----")
for element in namnlista:
    if len(element) < 4:
        continue
    else:
        print(element)
