import csv

zaznamy = [
    {"jmeno": "Jana Novakova", "Oddeleni": "IT", "Plat": 55000},
        {"jmeno": "Petr Svoboda", "Oddeleni": "Finance", "Plat": 62000},
        {"jmeno": "Marie Dvořáková", "Oddeleni": "IT", "Plat": 58000},
    ]

with open("zamestnanci.csv", "w", encoding="utf-8", newline="") as f:
    filenames = ["jmeno", "Oddeleni", "Plat"]
    writer = csv.DictWriter(f, fieldnames=filenames)
    writer.writeheader()
    writer.writerows(zaznamy)