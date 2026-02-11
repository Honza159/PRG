def dvojkova(x):
    y = ""
    while x > 0:
        y = str(x % 2) + y
        x //= 2
    return y
def osmickova(x):
    y = ""
    while x > 0:
        y = str(x % 8) + y
        x //= 8
    return y
def sestnackova(x):
    y = ""
    while x > 0:
        y = str(x % 16) + y
        x //= 16
    return y
def soustava():
    while True:
        print("--->soustavy<---")
        print("0 - konec")
        print("1 - pokračovat")
        volba1 = input("zadej číslo: ")

        a = ""
        b = ""
        c = ""
        d = ""
        if volba1 == "0":
            print("konec")
            break
        if volba1 != "1":
            print("neumíš čísla 0 a 1, pokračuj dál")
            volba1 = "1"
        if volba1 == "1":
            x = int(input("zadej číslo v desítkové soustavě: "))
            a = dvojkova(x)
            b = osmickova(x)
            c = x
            d = sestnackova(x)

        print(f"Výsledek ve dvojkové: {a}")
        print(f"Výsledek v osmičkové: {b}")
        print(f"Výsledek v desítkové: {c}")
        print(f"Výsledek v šestnáckové: {d}")
        print("")

soustava()
