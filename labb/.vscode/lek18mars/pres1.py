def wave_text(text):
    """Return a text with interchanging capital and lowercase letters.

    >>> wave_text("kajak")
    'KaJaK'
    >>> wave_text("kanot")
    'KaNoT'
    >>> wave_text("python")
    'PyThOn'
    """
    lst = [bokstav for bokstav in enumerate(text)]
    for index, bokstav in lst:
        jamnt = index % 2 == 0
        if jamnt:
            lst[index] = bokstav.upper()
        else:
            lst[index] = bokstav.lower()
    return "".join(lst)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
