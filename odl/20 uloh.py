slovnik = {
    "jméno": "Jan",
    "věk": 67,
    "město": "Česká Lípa"
}
print(slovnik)


auto = {
    "značka": "Škoda",
    "rok": 2020
}
print(auto["značka"])


student = {"jméno": "Kuba"}
print(student)

student["věk"] = 18
print(student)

student["věk"] = 19
print(student)

del student["věk"]
print(student)

mesta = {
    "a": 6767,
    "b": 6768,
    "c": 6769,
    "d": 6770,
    "e": 6771
}
mesta["f"] = 6772
print(mesta)

print(mesta)


slovniik = {
    1: 1**2,
    2: 2**2,
    3: 3**2,
    4: 4**2,
    5: 5**2
}
print(slovniik)

barvy = {
    "červená": "red",
    "modrá": "blue"
}
a = input("anglický překladač. (červená/modrá): ")
while True:
    if a == "červená":
        print(barvy["červená"])
        break
    elif a == "modrá":
        print(barvy["modrá"])
        break
    else:
        a = input("anglický překladač. (červená/modrá): ")


osoba = {"jmeno": "Eva", "vek": 25}
if osoba["vek"]:
    print("věk tam je")

trida = {
    "Tomáš1": 5,
    "Tomáš2": 4,
    "Tomáš3": 5,
    "Tomáš4": 2,
    "Tomáš5": 1,
    "Tomáš6": 3,
    "Tomáš7": 4
}
print(sum(trida.values())/6)


studenti = {
    "student1": {
        "jmeno": "Jan",
        "vek": 17,
        "predmety": ["Matematika", "Programování", "Angličtina"]
    },
    "student2": {
        "jmeno": "Tereza",
        "vek": 16,
        "predmety": ["ČJ", "Dějepis", "Biologie"]
    },
    "student3": {
        "jmeno": "Tomáš",
        "vek": 18,
        "predmety": ["Fyzika", "Chemie", "Matematika"]
    }
}


a = {1: 2}
b = {2: 3}
a.update(b)
print(a)



