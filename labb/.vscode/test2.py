# reference by value

a = ['a', 'b', 'c']
b = a
spara = b.pop()

# båda ändradet

a = ['a', 'b', 'c']
b = a[:]
spara = b.pop()

# bara b ändrades

a = ['a', 'b', 'c']
b = a.copy
spara = b.pop()

# punkten . betyder att nu kommer det en metod. objektet b har en metod som heter pop.

print