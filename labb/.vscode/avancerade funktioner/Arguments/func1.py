def plus(x, y=0, z=0):
    return x + y + z


# Positionella argument
print(plus(10, 20, 30))

# 1 Positionellt, 1 Nyckelord
print(plus(10, z=999))

# 3 Positionella, 1 Nyckelord
print("a", "b", "c", sep=" -- ")
