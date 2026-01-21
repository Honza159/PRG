locations =  {
"les": "Tmavý les plný tajemství.",
"Jeskyně": "Vlhká jeskyně s ozvénou.",
"hrad": "Starý hrad s duchy.",
"vesnice": "Poklidná vesnice s přátelskými obyvateli."
}
visited = []

print("Vitej v dobrodružné hře")
print("Prozkoumej všechny lokace.")
while True:
    print("\nDostupné lokace:")
    for loc in locations:
        if loc not in visited:
            print(f" - {loc}")


    choice = input("Kam chceš jit? (nebo napiš 'konec'): ").strip().lower()

    if choice == "konec":
        print("Hra ukončena.")
        break
    elif choice in locations and choice not in visited:
        visited.append(choice)
        print(f"\n{locations[choice]}")
        if len(visited) == len(locations):
            print("Gratuluji Navštívil jsi všechny lokace.")
            break
    elif choice in visited:
        print("Tuto lokaci jsi už navštívil")
    else:
        print("Neplatná volba.")