def kalkulacka():
    while True:
        print("--->lepší kalkulačka (snad)<---")
        print("1 - sčítání")
        print("2 - odčítání")
        print("3 - násobení")
        print("4 - dělení")
        print("0 - konec")
        volba = input("zadej číslo: ")

        if volba == "0":
            print("konec")
            break

        a = float(input("Zadej první číslo (pro desetinou čárku piš '.' ): "))
        b = float(input("Zadej druhé číslo (pro desetinou čárku piš '.' ):  "))

        if volba == "1":
            vysledek = scitani(a, b)
        elif volba == "2":
            vysledek = odcitani(a, b)
        elif volba == "3":
            vysledek = nasobeni(a, b)
        elif volba == "4":
            vysledek = deleni(a, b)
        else:
            print("špatná volba, teď sčítáš")
            vysledek = scitani(a, b)

        print(f"Výsledek: {vysledek}")


def scitani(a, b):
    return a + b
def odcitani(a, b):
    return a - b
def nasobeni(a, b):
    return a * b
def deleni(a, b):
    if b == 0:
        return "nejde dělit nulou"
    return a / b


kalkulacka()
