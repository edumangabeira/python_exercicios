'''
cálculo de medidas de dispersao, aceita listas como entrada
'''
import Centralidade
import math


class Dispersao:

    def __init__(self):
        self.freq = []

    def variancia(self, freq):
        self.media = Centralidade.media(freq)
        media = self.media
        soma = 0
        for i in freq:
            soma = soma + (media - freq) ** 2

        return soma / len(freq)

    def desvio_padrao(self, freq):
        return math.sqrt(self.variancia(freq))
