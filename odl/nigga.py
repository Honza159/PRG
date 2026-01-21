zacatek = int(input("začátek: "))
konec = int(input("konec: "))

for i in range(zacatek, konec):
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        print(str(i) + ',')


