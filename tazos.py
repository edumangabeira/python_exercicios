import random as rd
import statistics as st

def colecionarTazos(experimentos, colecionaveis):

    obtidos = []
    repetidos = []
    tentativas = 0

    while(len(obtidos) < 20):

        novo = rd.randint(1, colecionaveis)
        if novo not in obtidos:
            obtidos.append(novo)
        else:
            repetidos.append(novo)
        tentativas += 1

    experimentos.append(tentativas)


experimentos = []
colecionaveis = 20
rep_experimento = 100000


for i in range(1, rep_experimento):
    colecionarTazos(experimentos, colecionaveis)

print(st.mean(experimentos))
