text = input("Zadej text: ").lower().strip()
klic = input("Zadej klic: ").lower().strip()
sifrovano = ""
desifrovano = ""

for i in range(len(text)):
    p = ord(klic[i % len(klic)]) - ord('a')
    sifrovano += chr((ord(text[i]) - ord('a') + p) % 26 + ord('a'))
    desifrovano += chr((ord(text[i]) - ord('a') - p) % 26 + ord('a'))

print("Zašifrováno:", sifrovano)
print("Dešifrováno:", desifrovano)