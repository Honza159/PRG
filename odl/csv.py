import csv
import json

zaznamy = [
    {"jmeno": "Jana Novakova", "Oddeleni": "IT", "Plat": 55000},
    {"jmeno": "Petr Svoboda", "Oddeleni": "Finance", "Plat": 62000},
    {"jmeno": "Marie Dvořáková", "Oddeleni": "IT", "Plat": 58000},
]

with open("zamestnanci.csv", "w", encoding="utf-8", newline="") as f:
    fieldnames = ["jmeno", "Oddeleni", "Plat"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(zaznamy)



with open("save.json", "r", encoding="utf-8") as file:
    data = json.load(file)
print(data)





data = {
    "player_x": 10,
    "player_y": 4,
    "player_gender": "male",
    "enemies": [],
    "settings": {
        "resolution": "HD",
        "volume": 0.5,
        "world_level": 1,
        "xp": 0,
        "next_lvl_xp": 100,
        "player_max_hp": 100,
        "player_lvl": 1,
        "enemies_killed": 0,
        "quest_count": 0,
        "player_current_hp": 100
    },
    "inventory": {
        "gold": 100,
        "attack": 20,
        "potions": 1
    },
    "current_map": "main"
}

with open("save.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)



with open("save.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print(data)



a = 5
try:
    print("hodnota a je:", a)
except:
    print("a není definována")