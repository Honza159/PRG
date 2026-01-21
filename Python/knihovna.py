policka = []
poradi = 0
def pridani():

    print("---> PŘIDÁVAČ KNIH <---")
    nazev = input("nyní napiš jméno knihy: ")
    autor = input("nyní napiš autora knihy: ")
    iban = input("nyní napiš iban knihy: ")

    return nazev, autor, iban

def knihovna():
    global poradi
    while True:
        print("---> KNIHOVNA <---")
        print("1 - Přidání knihy do poličky")
        print("2 - Náhled do poličky")
        print("0 - Konec")
        volba = input("Zadej číslo: ")

        if volba == "0":
            print("Konec programu.")
            break

        elif volba == "1":
            nazev, autor, iban = pridani()
            policka.append((str(poradi), nazev, autor, iban))
            print(f"Kniha se jménem {nazev} byla přidána do knihovny")
            poradi += 1
        elif volba == "2":
            print(policka)
knihovna()



