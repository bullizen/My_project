knights = {"gallahad": "the pure", "robin": "the brave", "nyckel": "varde"}
#   //// Unpacking av tupeln
for nyckel, varde in knights.items():
    print(nyckel, varde)

print("---")

#   /// Lat tupeln vara en tupel
for tpl in knights.items():
    print(tpl[0], tpl[1])

print("---")

# Om jag vill andra, vanligt monster

for nyckel, varde in knights.items():
    knights[nyckel] = varde.upper()

print(knights)