radky = 0
slova = 0
znaky = 0
with open("praha.txt", "r", encoding="utf-8") as f:
    text = f.read()
    text_lower = text.lower()
    pocet = text_lower.count("praha")

    radky = text.count("\n") + 1
    slova = len(text.split())
    znaky = len(text)

print(f"{pocet}x slovo praha.")
print("řádky:", radky, "slova:", slova, "znaky:", znaky)