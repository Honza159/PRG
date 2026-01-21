Abeceda = "abcdefghijklmnopqrstuvwxyz"
Nova_abeceda = ""
message = input("Tvoje slovo na sifrovani: ").lower()
klic = int(input("O kolik: "))

klic = klic % 26
Nova_abeceda = Abeceda[klic:] + Abeceda[:klic]


sifra = ""
for znak in message:
    if znak == " ":
        sifra += " "
    elif znak in Abeceda:
        index = Abeceda.index(znak)
        sifra += Nova_abeceda[index]
    else:
        sifra += znak

print("Zašifrovaná zpráva:", sifra)
