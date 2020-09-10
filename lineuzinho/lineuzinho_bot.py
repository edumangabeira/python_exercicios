# -*-coding:"utf-8"-*-
# import pymongo
import tweepy
import time
import random

# joguinho do papel com elementos da grande família!!!!!!!!!!

'''
Quem
Com quem
Fazendo
Onde
Chegou (alguém)
E disse
Moral da história

'''


def popozonize(arqs):

    # testando tempo de execução
    start = time.time()
    conto = ""

    # descobrir como otimizar a manipulação do arquiv
    for arq in range(0, len(arqs)):
        # termo aleatório do arquivo atual
        rodada_atual = open(arqs[arq], "r")
        line_1 = rodada_atual.read().splitlines()
        str_arq = random.choice(line_1)
        rodada_atual.close()

        # popozonize
        conto = conto + "\n" + str_arq

    # testando tempo de execução
    end = time.time()
    print(end - start)

    return conto

# escrever função que junte as frases q provavelmente façam mais sentido


if __name__ == "__main__":

    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    quem = "nomes.txt"
    com_quem = "nomes_2.txt"
    fazendo = "fazendo.txt"
    onde = "lugares.txt"
    chegou_alguem = "nomes_3.txt"
    e_disse = "frases_1.txt"
    moral = "frases_2.txt"

    historia = [quem, com_quem, fazendo, onde, chegou_alguem, e_disse, moral]

    while(True):
        lineuzinho = popozonize(historia)
        lineuzar = api.update_status(status=lineuzinho)
        time.sleep(900)
