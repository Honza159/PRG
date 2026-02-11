seznam = []

for i in range (5):
    a = input("Kdo jseš: ")
    b = input("V kolik přicházíš nebo odcházíš (např. 12:00): ")
    seznam.append([a,b])
print(seznam)


while True:
    y = input("Jméno osoby nebo exit: ")
    if y == "exit":
        break
    for k in range (len(seznam)):
        if y==seznam[k][0]:
            print(seznam[k])







