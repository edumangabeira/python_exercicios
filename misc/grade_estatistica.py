# -*-coding:utf-8-*-
# montar uma grade bonita do curso
from bs4 import BeautifulSoup
import requests
# import csv

req = requests.get("https://www.siga.ufrj.br/sira/repositorio-curriculo/05697564-92A4-F79D-6C07-44FBBC4838FE.html")


# não tô conseguindo acessar a página q eu preciso
'''https://www.siga.ufrj.br/sira/temas/zire/frameConsultas.jsp?mainPage=/repositorio-curriculo/05697564-92A4-F79D-6C07-44FBBC4838FE.html'''
soup = BeautifulSoup(req.text, features="html.parser")
'''
listas com as materias que eu almejo completar
'''
'''
primeiro = ["MAD124", "MAD233", "MAB241", "MAD114"]
segundo = ["FIW123", "MAC106", "MAA114", "MAE125", "MAB243"]
terceiro = ["MAB489", "MAB231", "MAC233", "MAE127"]
quarto = ["MAD236", "MAA240", "MAD351", "MAD352", "MAB491", "MAA355", "MAD474"]
quinto =
optativas_6 = ["MAD478", "MAD418"]
sexto =
sexto = sexto.append(optativas_6)
optativas_7 = ["MAB368", "MAB518", "MAB529"]
setimo =
setimo = setimo.append(optativas_7)
oitavo = ["MAW485", "MAE242"]

obrigatorias_cr = 12
optativas_cr = 0
'''
print(soup.find_all("a", class_="linkNormal"))
''' a tag que eu quero é <b><\b>'''

with open("GradeCurricular.csv", "w") as csv_file:
    # writer = csv.writer()
    pass
