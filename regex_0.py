# -*-coding:utf8-*-
# import re
import random
'''
- fazer gerador randômico de caracteres esquisitos no meio das palavras

  * usar o dicionário.txt que está na mesma pasta

'''
# insere caracteres estranhos ao novo dicionario


def confusao(palavra, file):
    estranhos = ['$', '@', '#', '.', '-', '[']
    palavra = palavra.lower()
    for letra in palavra:

        # ele esta imprimindo como lista dessa forma, como mudar?
        '''estranho = random.choice(estranhos)
        escolhas = [letra, estranho]
        random_char = random.choices(escolhas, weights=[10, 1])'''
        file.write(letra)


# cria um segundo arquivo removendo caixa alta
# ##### REFAZER USANDO BLOCOS DE PROCESSAMENTO(CHUNKS)
with open("ptbr_dicionario.txt", 'r') as f_read:
    with open("v_confuso.txt", 'w') as f_write:
        novo_dicionario = [confusao(palavra, f_write) for palavra in f_read]


'''
- acentuar palavras seguindo regras do português, quando possível
'''
'''
def ditongo_aberto():
    pass
https://www.figuradelinguagem.com/gramatica/10-regras-de-acentuacao/
'''
