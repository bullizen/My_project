# Exercise 5: Check if the first and last number of a list is the same

# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

def forstasistanummer(nummerlista):
    print("Given lista", nummerlista)

    forsta_nummer = nummerlista[0]
    sista_nummer = nummerlista[-1]

    if forsta_nummer == sista_nummer:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]
print("Resultatet är", forstasistanummer(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("Resultatet är", forstasistanummer(numbers_y))

# def first_last_same(numberList):
#     print("Given list:", numberList)
    
#     first_num = numberList[0]
#     last_num = numberList[-1]
    
#     if first_num == last_num:
#         return True
#     else:
#         return False

# numbers_x = [10, 20, 30, 40, 10]
# print("result is", first_last_same(numbers_x))

# numbers_y = [75, 65, 35, 75, 30]
# print("result is", first_last_same(numbers_y))