from dataclasses import dataclass

@dataclass
class Test:
    a: int

d = {
    0: Test(1)
}

d[0].animal = 'dog'
m = d[0]
m.color = 'brown'

print(d[0].animal)
print(m.animal)

print(d[0].color)
print(m.color)
