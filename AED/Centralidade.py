'''
cálculo de medidas de tendência central, aceita listas como entrada
'''


class Centralidade:

    def __init__(self):
        self.freq = []

    def media(self, freq):
        soma = 0
        for valor in freq:
            soma = soma + valor

        return soma / len(freq)

    def mediana(self, freq):
        if (len(freq) % 2 != 0):
            return freq[len(freq / 2)]
        else:
            valores_medios = freq[len(freq / 2)] + freq[len((freq / 2) + 1)]
            return valores_medios / 2
