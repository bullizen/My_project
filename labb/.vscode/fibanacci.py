# Fibonacci series:
# the sum of two elements defines the next

# unboxing
x = 0, 1, 3, 4
a, b, c, d = x
while a < 10:
    print(a, b)
    # unboxing! högra delen först
    a, b = b, a + b
print("---")
print(x)
print(type(x))
