while True:
    f = input("Chceš sčítat: (ano/ne) ")
    if f == "ano":
        break
    g = input("Chceš odčítat: (ano/ne) ")
    if g == "ano":
        break
    h = input("Chceš násobit: (ano/ne) ")
    if h == "ano":
        break
    i = input("Chceš dělit: (ano/ne) ")
    if i == "ano":
        break
    j = input("Chceš na druhou: (ano/ne) ")
    if j == "ano":
        break
if f == "ano":
    a = int(input("1. číslo: "))
    b = int(input("2. číslo: "))
    def kalkulacka(a,b):
        d = a + b
        print(d)
if g == "ano":
    a = int(input("1. číslo: "))
    b = int(input("2. číslo: "))
    def kalkulacka(a,b):
        d = a - b
        print(d)
    kalkulacka(a,b)
if h == "ano":
    a = int(input("1. číslo: "))
    b = int(input("2. číslo: "))
    def kalkulacka(a,b):

        d = a * b
        print(d)
    kalkulacka(a,b)
if i == "ano":
    a = int(input("1. číslo: "))
    b = int(input("2. číslo: "))
    def kalkulacka(a,b):

        d = a / b
        print(d)
    kalkulacka(a,b)
if j == "ano":
    a = int(input("1. číslo: "))
    b = int(input("2. číslo: "))
    def kalkulacka(a,b):
        d = a ** b
        print(d)
    kalkulacka(a,b)