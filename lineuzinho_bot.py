# -*-coding:"uft8"-*-
# import pymongo
import tweepy
import time
import random

# bd com frases da grande familia
# bd com recomendações diárias ou discurso motivacional


def popozonize(db_generico, db_lineuzinho):

    # testando tempo de execução
    start = time.time()

    # descobrir como otimizar a manipulação do arquivo
    with open(db_generico, "r") as arq1:
        with open(db_lineuzinho, "r") as arq2:

            # primeiro termo aleatório
            line_1 = arq1.read().splitlines()
            str_1 = random.choice(line_1)

            # segundo termo aleatório
            line_2 = arq2.read().splitlines()
            str_2 = random.choice(line_2)

            # popozonize
            recom_diaria = str_1 + " " + str_2

    # testando tempo de execução
    end = time.time()
    print(end - start)

    return recom_diaria

# escrever função que junte as frases q provavelmente façam mais sentido


if __name__ == "__main__":

    consumer_key = 'buLO65zp0MpvY8DtHU5S3aPQJ'
    consumer_secret = 'R9jSkLr42DB9cIZ3BfAVt6Yy5pNxd61SDBKuupWCDNPzoxmePi'
    access_token = '1017478115126317056-7HHdMDu3aKeYGtvsCkOPP7fJnZr8h9'
    access_token_secret = 'IEXXdAi2KBV7T3ldQG0bkistkkAy498bSxONAkf7VqpdB'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    db_generico = "generico.txt"
    db_lineuzinho = "lineuzinho.txt"

    while(True):
        lineuzinho = popozonize(db_generico, db_lineuzinho)
        lineuzar = api.update_status(status=lineuzinho)
        time.sleep(900)
