fraze = input("Tvoje fráze: ").lower()
nalezeno = ["_" if ch != " " else " " for ch in fraze]

while True:
    pismeno = input("Tvoje písmeno: ").lower()
    if pismeno == "exit":
        print("Ukončeno.")
        break

    if pismeno in fraze:
        pozice = [i + 1 for i, ch in enumerate(fraze) if ch == pismeno]
        for i in pozice:
            nalezeno[i - 1] = pismeno
        print(f"Písmeno '{pismeno}' se nachází na místech: {pozice}")
    else:
        print(f"Písmeno '{pismeno}' se ve frázi nenachází.")

    print(" ".join(nalezeno))

    if "".join(nalezeno) == fraze:
        print(f"Gratulace! Našel jsi celou frázi: {fraze}")
        break
