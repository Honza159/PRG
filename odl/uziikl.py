import bitcoin
import requests
import re
import datetime

urls = [
"https://rpishop.cz/raspberry-pi-4/1598-raspberry-pi-4-model-b-4gb-ram.html",
"https://rpishop.cz/raspberry-pi-4/1599-raspberry-pi-4-model-b-2gb-ram.html",
"https://rpishop.cz/535838/raspberry-pi-5-2gb-ram/",
"https://rpishop.cz/raspberry-pi-5/6497-raspberry-pi-5-4gb-ram.html",
"https://rpishop.cz/535824/raspberry-pi-pico-2/",
]


for url in urls:
        html = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}).text

        match = re.search(r'product:price:amount[^0-9]*(\d+[.,]?\d*)', html)


        if match:
            with open("Bitcoin.txt", encoding="utf-8" mode='a') as file:
                file.write(f"{datetime.datetime.now()}{match.group(1)} Kč")

