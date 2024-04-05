# "if x != y" Om x är lika med y, tex 1 och 1. 
l3 = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(l3)

# Start, en sa enkel list comprehension som möjligt
l1 = [y for y in [3, 1, 4]]
print(l1)

# Filtrera bort varden med if efter "foor-loopen".
l2 = [y for y in [3, 1, 4] if 1 != y]
print(l2)