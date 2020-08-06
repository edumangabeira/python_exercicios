import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.gameskinny.com/1o5tb/ffxii-the-zodiac-age-hunt-club-and-trophy-rare-game-guide'
pagina = requests.get(url)
soup = BeautifulSoup(pagina.text, features="lxml")
tabelas = soup.findAll('table')

# locais das hunts
locais = pd.read_html(str(tabelas[1]))
print(locais[0])
locais[0].to_csv(r'C:\Users\Eduardo\Desktop\HuntLocations.csv')
