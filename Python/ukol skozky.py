from pathlib import Path

slozka = Path("programování v pátek")
slozka.mkdir(exist_ok=True)

soubor = slozka / "datum.txt"
soubor.write_text(str("06.07.2067"))

print("Složka a soubor byly vytvořeny.")