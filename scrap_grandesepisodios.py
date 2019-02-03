from bs4 import BeautifulSoup
import requests
# import re

req = requests.get("https://pt.wikipedia.org/wiki/Lista_de_epis%C3%B3dios_de_A_Grande_Fam%C3%ADlia")

soup = BeautifulSoup(req.text, "html.parser")
# soup.find_all("td", class_="wikitable").text

'''
titulos = soup.select("td")
for titulo in titulos:
    titulo = titulo.getText()
    if not titulo.isdigit():
        moral = titulo
        with open("moral.txt", "a") as arq:
            arq.write(moral)
'''
'''
arq = open("frases.txt", 'r')
arq_2 = open("frases_2.txt", 'w')
for palavra in arq:
    palavra = palavra.lower()
    palavra = "\nmoral da história:" + palavra
    print(palavra)
    arq_2.write(palavra)
arq.close()
arq_2.close()
'''
'''
arq = open("nomes_2.txt", 'r')
arq_2 = open("nomess_2.txt", 'w')
for palavra in arq:
    palavra = palavra.lower()
    palavra = "\ncom " + palavra
    print(palavra)
    arq_2.write(palavra)
arq.close()
arq_2.close()
'''
