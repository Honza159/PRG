Abeceda = "abcdefghijklmnopqrstuvwxyz"
message = input("Vložte text: ").lower()
klic = int(input("Posun: ")) = % 26
Nova_abeceda = Abeceda[klic:] + Abeceda[:klic]
sifra = ""
for znak in message:
    if znak == " ":
        sifra += " "
    elif znak in Abeceda:
        sifra += Nova_abeceda[Abeceda.index(znak)]
print("Zašifrovaná zpráva:", sifra)
