def multiplication_or_sum(num1, num2):
    # calculate product of two number
    product = num1 * num2
    # check if product is less then 1000
    if product <= 1000:
        return product
    else:
        # product is greater than 1000 calculate sum
        return num1 + num2

# first condition
result = multiplication_or_sum(20, 30)
print("The result is", result)

# Second condition
result = multiplication_or_sum(40, 30)
print("The result is", result)

# def exercise1(x, y):
#     product = x * y

# if product <= 1000:
#     return product
# else:
#     return x + y

# result = exercise1(20, 30)
# print("The result is", result)

# result = exercise1(40, 30)
# print("The result is", result)