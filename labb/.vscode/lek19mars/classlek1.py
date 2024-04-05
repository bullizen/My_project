class SifferOperation:
    def __init__(self, num, text=None) -> None:
        self._num = num
        self._text = text

    def __repr__(self) -> str:
        return f"SifferOperation({self._num, self._text})"

    def __str__(self) -> str:
        return "str: " + str(self._num) + self._text

    def __eq__(self, __value: object) -> bool:
        return self._num == __value._num


s1 = SifferOperation(2, "Hej")
s2 = SifferOperation(2, "Hopp")

lika = s1 == s2


# s_as_string = str(s1)
