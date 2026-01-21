fráze = input("tvoje fráze: ")
hledáš = input("která písmena ve frázi hledáš: ")
for i in hledáš:
    a=False
    for j in fráze:
        if i == j:
           a = True
           break
    if a:
        print(f"Ano, písmeno {i} je ve frázi")
    else:
        print(f"Ne, písmeno {i} není ve frázi")
