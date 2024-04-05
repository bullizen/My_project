# Exercise 3: Return multiple values from a function
# Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.


def calculation(x, y):
    addition = x + y
    subtraction = x - y
    return addition, subtraction

res = calculation(100, 200)
print(res)

# Separate return values with a comma.