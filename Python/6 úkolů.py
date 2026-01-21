"""
a, b, c=map(int,input().split())
s = a + b + c
print(f"součet={s}, průměr={s/3:.2f}")

m=int(input())
h,m =divmod(m,60)
print(f"{h}:{m:02d}")

c=float(input())
d = c*0.21
print(f"DPH={d:.2f}, s DPH={c+d:.2f}")

a,b=map(float,input().split())
print(f"Obvod: {2*(a+b):.2f}, Obsah: {a*b:.2f}")

import math
a,b=map(float,input().split())
x=a*b
print(f"{a**2:g}, b3={b**3:.2f}, odm={math.sqrt(x):.2f}" if x>=0 else "nelze odmocnit záporné")

c, os=map(float,input().split())
print(f"každý={math.ceil(c/os)} Kč")

n,m=map(int,input().split())
print("Chyba: dělení nulou") if m == 0 else print(f"/, //, % = {n/m}, {n//m}, {n%m}")

c=float(input())
print(f"F={(c*9/5)+32:.2f}, K={c+273.15:.2f}")

x, op, y = input().split()
x=float(x);y=float(y)
if op in "/%//" and y ==0:print("Dělení nulou")
else:
    print(int(x+y) if op == "+" else int(x-y) if op == "-" else int(x*y) if op == "*" else x/y if op == "/" else x**y if op == "**" else x%y if op == "%" else x//y)

a, b, c = map(int, input().split())
if a == 0:
    print("Není kvadratická rovnice")
else:
    D = b*b - 4*a*c
    if D < 0:
        print("Žádné reálné řešení")
    elif D == 0:
        x = -b / (2*a)
        print(x)
    else:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print(x1, x2)
"""

#1.
print(7+3*4-2**3)

#2.
n = 12345
m = 97
print("Chyba: dělení nulou") if m == 0 else print(f"/, //, % = {n/m}, {n//m}, {n%m}")

#3.
sekundy = 10000
h = sekundy // 3600
m = (sekundy % 3600) // 60
s = sekundy % 60
print(f"{h:02d}:{m:02d}:{s:02d}")

#4.
c=2899
d = c*0.21
print(f"DPH={d:.2f}, s DPH={c+d:.2f}")

#5.
c=-7.5
print(f"F={(c*9/5)+32:.2f}, K={c+273.15:.2f}")

#6.
a = 5.2
b = 3.8
print(f"Obvod: {2*(a+b):.2f}, Obsah: {a*b:.2f}")

