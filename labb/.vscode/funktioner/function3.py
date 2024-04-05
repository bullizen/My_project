# None representerar inget alls
print(type(None))


# grad ska ha standardvardet len(ord) / 2
# vi vet att anvandaren inte skickade in grad om den ar None
def palindromish(ord, grad=None):
    if grad == None:
        grad = len(ord) // 2

    return True  # det ar fel!


palindromish("mamma")

palindromish("XqwertyX", 1)
