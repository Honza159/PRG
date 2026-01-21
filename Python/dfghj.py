a = 1,2,3
pary = [("jmeno","Tomáš"), ("vek",18)]
osoba = dict(pary)
klice = ["A", "B", "C"]
vse_ma_zero = dict.fromkeys(klice, 0)
osoba["skola"] = "SPS"
osoba["vek"] = 19
del osoba["skola"]
osoba.pop("vek", None)
osoba.keys()
osoba.values()
osoba.items()

a = {"jmeno": "Franta", "vek": 18}
b = {"věk": 19, "trida": "2.B"}
a.update(b)
c = a | {"prumer": 1.75}
znamky = {"Matematika": 1, "Python": 2, "fyzika": 1}

for predmet in znamky:
    print(predmet, znamky[predmet])

for predmet, znamka in znamky.items():
    print(predmet, znamka)
vyborne = {p: z for p, z in znamky.items() if z == 1}

trida= {
    "student_001" : {
        "jmeno": "Franta",
        "rocnik": 4,
        "znamky": {"matematika": 1, "Python": 2},
    },
    "student_002" : {
        "jmeno": "Tomas",
        "rocnik": 2,
        "znamky": {"matematika": 4, "Python": 1}
    },
}
trida["student_001"]["znamky"]
skupiny = {}
for jmeno, predmet in [("Franta", "Python"), ("Franta", "Matematika"), ("Tomas", "Python")]:
    skupiny.setdefault(jmeno, []).append(predmet)

validni = {("Franta", "Novák"): 1}
merged = a | b

osoba = {
    "jmeno": "Franta Novák",
    "vek": 18,
    "trida": "2.B"
}
osoba["vek"] +=1
print(osoba["jmeno"])
osoba.get("email", "nezadáno")
print(osoba)
kontakt = {"jmeno":"pepa dvorak", "telefon":"777 123 456"}


kontakt.pop("telefon")



