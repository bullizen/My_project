# palindromish.py
def palindromish(text, grade=None):
    if not isinstance(text, str):
        raise TypeError("Ange en strang")
    
    if grade is None:
        grade = len(text) // 2

    # Tog bort i refactoring-fasen
    # if text == "":
    #     return True
    
    prefix = text[:grade]
    suffix = text[-grade:]
    suffix = suffix[::-1]

    return prefix == suffix