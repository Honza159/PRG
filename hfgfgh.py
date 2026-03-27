print("(1. + 2.)x(3. + 4.)")

a = complex(input("Zadej první číslo: "))
b = complex(input("Zadej druhé číslo: "))
c = complex(input("Zadej třetí číslo: "))
d = complex(input("Zadej čtvrtý číslo: "))

plus = ((a + b) + (c + d))
minus = ((a + b) - (c + d))
krat = ((a + b) * (c + d))
deleno = ((a + b) / (c + d))

print(f"{a} + {b} = ({a} + {c}) + ({b} + {d}) = {plus}")
print(f"{a} - {b} = ({a} - {c}) + ({b} - {d}) = {minus}")
print(f"{a} * {b} = ({a} * {c}) + ({a} * {d}) + ({b} * {c}) + ({b} * {d}) = {krat}")
print(f"{a} / {b} = (({a} + {b}) / ({c} + {d})) * (({c} - {d})/({c} - {d})) = {deleno}")