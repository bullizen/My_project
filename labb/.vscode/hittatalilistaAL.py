def find_greater_than(in_list, threshold):
    ut_list = []
    # fyll ut_list med alla varden storre an threshold
    for element in in_list:
        if element > threshold:
            ut_list.append(element)

    return ut_list


x = [-3, 2, 8, 15, 31, 5, 4, 8]

ut = find_greater_than(x, 5)
print(type(ut))
print(ut)
