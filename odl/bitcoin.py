import requests
from bs4 import BeautifulSoup
import datetime

url = "https://www.kurzy.cz/komodity/bitcoin-graf-vyvoje-ceny/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

last_usd_elem = soup.find(id="last_usd")-*


if last_usd_elem:
    bitcoin_usd = last_usd_elem.text.strip()
    with open("Bitcoin.txt", encoding="utf-8", mode='a') as file:
        file.write(f"{datetime.datetime.now()}{group(1)} Kč")


