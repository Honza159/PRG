with open("praha.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()

pocet = text.count("praha")
print(f"{pocet}x slova praha")