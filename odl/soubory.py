from pathlib import Path
from datetime import datetime

with open("pozdrav.txt", "w", encoding="utf-8") as f:
    f.write("Ahoj Franto Nováku!\n")
    f.write("Zdraví tvoje aplikace python.\n")
print("Soubor pozdrav.txt byl vytvořen a zaspán.")


with open("pozdrav.txt", "r", encoding="utf-8") as f:
    obsah = f.read()
print(obsah)

cesta = Path("odl") / "Data"/ "osoby" / "seznam.txt"
print(cesta)


with open(cesta, "w", encoding="utf-8") as f:
    f.write("ukol\n")
print("Soubor ukol.txt byl vytvořen a zaspán.")

with open(cesta, "r", encoding="utf-8") as f:
    obsah = f.read()
print(obsah)

with open("denik.txt", "w", encoding="utf-8") as soubor:
    soubor.write("Dnes bylo krásné počasí.\n")
    soubor.write("Šel jsem na procházku do přírody.\n")

with open("denik.txt", "r", encoding="utf-8") as soubor:
    obsah = soubor.read()
    print(obsah)


cesta = Path("odl/Data/denik.txt")
cesta.parent.mkdir(parents=True, exist_ok=True)
while True:
    zprava = input("Zadej text (nebo 'konec'): ")
    if zprava.lower() == "konec":
        break

    with open(cesta, "a", encoding="utf-8") as soubor:
        soubor.write(f"{datetime.now()} {zprava}\n")

print("\nObsah souboru:")
print(cesta.read_text(encoding="utf-8"))