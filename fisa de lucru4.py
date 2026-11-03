from enum import Enum
class Anotimp(Enum):
    PRIMAVARA=1
    VARA=2
    TOAMNA=3
    IARNA=4
a=Anotimp.PRIMAVARA
b=Anotimp.VARA
c=Anotimp.TOAMNA
d=Anotimp.IARNA
print(a.name, a.value)
print(b.name, b.value)
print(c.name, c.value)
print(d.name, d.value)