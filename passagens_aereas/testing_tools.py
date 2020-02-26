from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def login(driver):

    with open("credentials.txt") as arquivo:
        linhas = arquivo.read().splitlines()
        usuario = linhas[0].partition('=')[2]
        senha = linhas[1].partition('=')[2]

    usuario = driver.find_element_by_name('session[username_or_email]')
    usuario.clear()
    usuario.send_keys(usuario)

    senha = driver.find_element_by_name('session[password]')
    senha.clear()
    senha.send_keys(senha)

    senha.submit()


# usar como último recurso
def crawler():
    driver = webdriver.Chrome(r'C:\Users\Eduardo\python_exercicios\passagens_aereas\chromedriver')
    driver.implicitly_wait(45)
    driver = driver.get("https://www.maxmilhas.com.br/busca-passagens-aereas/RT/GIG/BOG/2020-07-14/2020-07-21/1/0/0/EC")
    print(driver)
    time.sleep(42)

    direto = "//label[contains(@data-gtm-vis-first-on-screen-8044998_628,'80772')]"
    if direto == None:
        return "essa companhias aéreas tão chatas hein"
    direto = driver.find_element_by_xpath(direto)
    direto.click()
    # https://www.guru99.com/xpath-selenium.html#1

    xpath = "//span[contains(@data-action,'search-result-total-outbound')]"
    try:
        # preco_da_passagem = driver.find_elements(By.CSS_SELECTOR, "BpkText_bpk-text__2NHsO.BpkText_bpk-text--lg__3vAKN.BpkText_bpk-text--bold__4yauk")
        preco_da_passagem = driver.find_element_by_xpath(xpath)
        print(preco_da_passagem)
    except:
        if(preco_da_passagem) == 'None':
            print('NoSuchElementException')
        else:
            print("excecao ao entrar na pagina")
            print("provavel que a pagina tenha checado por atividade de um bot")
        time.sleep(800)

    print(preco_da_passagem.text)

    # for preco in preco_da_passagem:
    #    print(preco_da_passagem.text)


crawler()


# NÃO DEU CERTO
'''
import requests
from bs4 import BeautifulSoup

# skyscanner
url = 'https://www.skyscanner.com.br/transporte/passagens-aereas/gig/bog/200714/200721/?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&ref=home'
page = requests.get(url)
# print(page.text)

soup = BeautifulSoup(page.text, 'html.parser')
print(soup.find_all("div"))
preco = soup.find_all("span", class_="BpkText_bpk-text__2NHsO BpkText_bpk-text--lg__3vAKN BpkText_bpk-text--bold__4yauk")
print(preco)
'''
