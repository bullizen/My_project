standard_input = "123"

x = int(input("Please eneter an interget: "))
# y = int(x)

# print("du skrev:", y, "den har typen", type(y))

# print("du skrev:", x, "den har typen", type(x))

if x < 0:
    x = 0
    print("Negative changed to zero")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")

print("Slut")