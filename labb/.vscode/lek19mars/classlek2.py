from dataclasses import dataclass

@dataclass()
class SifferOperation:
    num: int
    text: str = None

s1 = SifferOperation(2, "Hej")
s2 = SifferOperation(2, "Hopp")

print(s1)

lika = s1 == s2