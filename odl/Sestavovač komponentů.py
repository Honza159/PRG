def sestava():
    while True:
        print("---> SESTAVOVAČ PC <---")
        print("1 - Pokračovat")
        print("0 - Konec")
        volba = input("Zadej číslo: ")

        if volba == "0":
            print("Konec programu.")
            break

        elif volba == "1":
            print("Nyní budeš zadávat svoje komponenty.")

            cpu = {
                "1": ("Itel A3", 1500),
                "2": ("Itel A5", 2000),
                "3": ("Itel A7", 3000),
                "4": ("Itel A9", 4500),
                "5": ("ARM R5", 2500),
                "0": ("Žádný", 0)
            }
            print("--- CPU ---")
            for k, v in cpu.items():
                print(f"{k} - {v[0]} ({v[1]} Kč)") #napsani dictionary cislo, nazev, cena
            CPU = input("Číslo CPU: ")

            ram = {
                "1": ("ASAS 3000Mhz", 1000),
                "2": ("ASAS 6000Mhz", 1600),
                "3": ("RSPAPER 3200Mhz", 1200),
                "4": ("KINGDOM FERY 4000Mhz", 1800),
                "5": ("PARRIOT SIGMATURE 5200Mhz", 2000),
                "0": ("Žádná", 0)
            }
            print("--- RAM ---")
            for k, v in ram.items():
                print(f"{k} - {v[0]} ({v[1]} Kč)")
            RAM = input("Číslo RAM: ")

            mb = {
                "1": ("ASAS 541235522657 ITEL", 2200),
                "2": ("ASAS 124534345243 ITEL", 2500),
                "3": ("RSPAPER 353453434343 ITEL", 2700),
                "4": ("KINGDOM 45234548443 ITEL", 3200),
                "5": ("PARRIOT 4534833438 ARM", 2800),
                "0": ("Žádná", 0)
            }
            print("--- Základní deska ---")
            for k, v in mb.items():
                print(f"{k} - {v[0]} ({v[1]} Kč)")
            MB = input("Číslo MB: ")

            gpu = {
                "1": ("MVIDEO ZTX 6767 6GB", 4000),
                "2": ("MVIDEO ZTX 6768 8GB", 5500),
                "3": ("MVIDEO ZTX 6769 10GB", 6500),
                "4": ("MVIDEO ZTX 6770 12GB", 8000),
                "5": ("ARM GR 3000", 3500),
                "0": ("Žádná", 0)
            }
            print("--- Grafická karta ---")
            for k, v in gpu.items():
                print(f"{k} - {v[0]} ({v[1]} Kč)")
            GPU = input("Číslo GPU: ")

            zdroj = {
                "1": ("ASAS 670W", 1200),
                "2": ("MZI 680W", 1300),
                "3": ("BDATA 700W", 1500),
                "4": ("WATERSONIC 800W", 1700),
                "5": ("MEGABIT 900W", 1900),
                "0": ("Žádný", 0)
            }
            print("--- Zdroj ---")
            for k, v in zdroj.items():
                print(f"{k} - {v[0]} ({v[1]} Kč)")
            ZDROJ = input("Číslo zdroje: ")

            hdd = {
                "1": ("CROSPAIR 1TB", 1000),
                "2": ("BDATA 1,5TB", 1300),
                "3": ("SUMSUNG 2TB", 1600),
                "4": ("VD ORANGE 2,5TB", 1900),
                "5": ("SUMSUNG 3TB", 2100),
                "0": ("Žádný", 0)
            }
            print("--- HDD ---")
            for k, v in hdd.items():
                print(f"{k} - {v[0]} ({v[1]} Kč)")
            HDD = input("Číslo HDD: ")

            ssd = {
                "1": ("CROSPAIR 500GB", 2000),
                "2": ("BDATA 700GB", 2500),
                "3": ("SUMSUNG 800GB", 3000),
                "4": ("VD ORANGE 999GB", 3500),
                "5": ("SUMSUNG 2TB", 5000),
                "0": ("Žádný", 0)
            }
            print("--- SSD ---")
            for k, v in ssd.items():
                print(f"{k} - {v[0]} ({v[1]} Kč)")
            SSD = input("Číslo SSD: ")


            doplnky = {
                "Chlazení": {
                    "1": ("AirCool 300", 800),
                    "2": ("WaterFlow 500", 1500),
                    "3": ("Silent Pro 700", 2200),
                    "4": ("ThermoKing 900", 2600),
                    "5": ("Arctic Blast 1200", 3200),
                    "0": ("Žádné", 0)
                },
                "Zvuková karta": {
                    "1": ("SoundMax 200", 500),
                    "2": ("ASAS Sound 5.1", 900),
                    "3": ("HyperX Audio 7.1", 1300),
                    "4": ("Razer SoundBlaster", 1600),
                    "5": ("SteelAudio Supreme", 2000),
                    "0": ("Žádná", 0)
                },
                "Bedna": {
                    "1": ("CoolerBox Mini", 900),
                    "2": ("MegaTower RGB", 1600),
                    "3": ("SilentCase Black", 2000),
                    "4": ("Thermaltake Pro", 2400),
                    "5": ("RGB Xtreme Glass", 2800),
                    "0": ("Žádná", 0)
                },
                "Monitor": {
                    "1": ("ViewTech 24''", 2500),
                    "2": ("SUMSUNG 27''", 4000),
                    "3": ("LG UltraGear 29''", 5200),
                    "4": ("ASUS ProArt 32''", 6500),
                    "5": ("MSI Curved 34''", 8000),
                    "0": ("Žádný", 0)
                },
                "Reprák": {
                    "1": ("Logitech 2.1", 1200),
                    "2": ("Razer Audio", 2000),
                    "3": ("Trust Sound 5.1", 2400),
                    "4": ("Edifier X5", 2800),
                    "5": ("SteelSeries Arena", 3500),
                    "0": ("Žádný", 0)
                },
                "Sluchátka": {
                    "1": ("HyperX Cloud", 1800),
                    "2": ("Razer Kraken", 2200),
                    "3": ("SteelSeries Arctis", 2500),
                    "4": ("Corsair Void", 2700),
                    "5": ("Logitech G Pro X", 3000),
                    "0": ("Žádná", 0)
                },
                "Myš": {
                    "1": ("Logitech G102", 800),
                    "2": ("Razer DeathAdder", 1300),
                    "3": ("Glorious Model O", 1600),
                    "4": ("SteelSeries Rival 3", 1900),
                    "5": ("CoolerMaster MM720", 2100),
                    "0": ("Žádná", 0)
                },
                "Klávesnice": {
                    "1": ("Redragon Kumara", 1000),
                    "2": ("HyperX Alloy", 1600),
                    "3": ("Logitech G413", 1900),
                    "4": ("Razer Huntsman", 2500),
                    "5": ("SteelSeries Apex", 2800),
                    "0": ("Žádná", 0)
                },
                "Webkamera": {
                    "1": ("Logitech C270", 900),
                    "2": ("A4Tech HD 1080p", 1200),
                    "3": ("Razer Kiyo", 1800),
                    "4": ("Elgato FaceCam", 3200),
                    "5": ("Logitech Brio 4K", 4000),
                    "0": ("Žádná", 0)
                },
                "Volant": {
                    "1": ("Logitech G29", 5000),
                    "2": ("Thrustmaster T300", 6500),
                    "3": ("Hori Apex", 3500),
                    "4": ("Fanatec CSL DD", 12000),
                    "5": ("MOZA R9", 15000),
                    "0": ("Žádný", 0)
                }
            }

            vybrane_doplnky = {}
            for nazev, moznosti in doplnky.items():
                print(f"--- {nazev.upper()} ---")
                for k, v in moznosti.items():
                    print(f"{k} - {v[0]} ({v[1]} Kč)")
                vybrane_doplnky[nazev] = input(f"Číslo pro {nazev}: ")

            celkem = (
                cpu[CPU][1] + ram[RAM][1] + mb[MB][1] + gpu[GPU][1] +
                zdroj[ZDROJ][1] + hdd[HDD][1] + ssd[SSD][1]
            )

            for nazev, volba in vybrane_doplnky.items():
                celkem += doplnky[nazev][volba][1]


            print("\n===================================")
            print("🖥️  Tvoje finální sestava PC:")
            print(f"CPU: {cpu[CPU][0]}")
            print(f"RAM: {ram[RAM][0]}")
            print(f"Základní deska: {mb[MB][0]}")
            print(f"Grafická karta: {gpu[GPU][0]}")
            print(f"Zdroj: {zdroj[ZDROJ][0]}")
            print(f"HDD: {hdd[HDD][0]}")
            print(f"SSD: {ssd[SSD][0]}")
            for nazev, volba in vybrane_doplnky.items():
                print(f"{nazev}: {doplnky[nazev][volba][0]}")
            print("===================================")
            print(f"💰 Celková cena sestavy: {celkem} Kč")
            print("===================================")

        else:
            print("Neplatná volba, zkus to znovu.")
sestava()