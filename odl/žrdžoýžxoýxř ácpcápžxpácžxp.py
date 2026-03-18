import zipfile
from pathlib import Path


def je_png(cesta):
    PNG_HLAVICKA = b'\x89PNG\r\n\x1a\n'
    try:
        with open(cesta, "rb") as f:
            return f.read(8) == PNG_HLAVICKA
    except OSError:
        return False


print(je_png("fotka.png"))

def kopiruj_soubor(zdroj, cil, velikost_bloku=65536):
    try:
        with open(zdroj, "rb") as src, open(cil, "wb") as dst:
            celkem = 0
            while True:
                blok = src.read(velikost_bloku)
                if not blok:
                    break
                dst.write(blok)
                celkem += len(blok)
        return celkem
    except FileNotFoundError:
        print(f"Soubor {zdroj} nebyl nalezen!")
        return 0
kopiruj_soubor("fotka.png", "kopie_fotky.png")




with zipfile.ZipFile('vigenere.zip', 'w', compression=zipfile.ZIP_DEFLATED) as zip_f:

    zip_f.write('Data/soubor.txt', arcname='Data/soubor.txt')

    for py_soubor in Path('src').rglob('*.py'):
        zip_f.write(py_soubor)

with zipfile.ZipFile('vigenere.zip', 'r') as zip_f:

    zip_f.printdir()
    nazvy = zip_f.namelist()
    with zip_f.open('Data/soubor.txt') as soubor:
        obsah = soubor.read().decode('utf-8')
    zip_f.extractall('vystupni_adresar')