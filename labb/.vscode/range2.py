# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, "equals", x, "*", n // x)
#             break
#         else:
#             # loop fell through without finding a factor
#             print(n, "is a prime number")

lst = [80, 20, 10, 5, 4]

hittat_tal = None

for element in lst:
    if element < 10:
        if hittat_tal is None:
            hittat_tal = element
    print(element)
