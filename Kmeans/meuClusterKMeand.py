from sklearn.cluster import KMeans
import numpy as np


# X = np.array([])

dados = []
with open("(VLIMPA)posicionamentos.csv") as arq:
    for linha in arq:
        linha = linha.replace("\n", "")
        dados_linha = linha.split(",")
        dados.append(dados_linha)
print(dados)

X = np.concatenate([dados])

# print(X)

orientacoes = [['-1', '1', '-1', '1', '1', '1', '1', '1', '1', '-1', '-1', '1', '0'], ['1', '-1', '1', '-1', '-1', '1', '-1', '-1', '0', '1', '-1', '-1']]

print(orientacoes)

X_2 = np.concatenate([orientacoes])

Y = np.concatenate(([X_2[0]], [X_2[1]]), axis=0)

kmeans = KMeans(n_clusters=2, random_state=0).fit(Y)
print(kmeans.labels_)
print(kmeans.predict(X))
