'''
Os níveis de um determinado hormônio que indica clinicamente um estado
de alto estresse, obtidos para 60 funcionários do Hospital Universitário,
estão relacionados a seguir(arquivo frequenciasAEDestresse.txt)

1.84 1.60 1.72 1.81 1.84 1.51 1.71 1.61 1.72 1.59
1.50 1.71 1.77 1.72 1.58 1.55 1.79 1.80 1.89 1.82
1.58 1.69 1.60 1.62 1.68 1.64 1.68 1.77 1.46 1.47
1.72 1.64 1.67 1.57 1.80 1.70 1.60 1.63 1.65 1.73
1.57 1.52 1.82 1.50 1.88 1.63 1.72 1.53 1.61 1.79
1.41 1.64 1.61 1.64 1.64 1.68 1.78 1.76 1.63 1.79

(a) Construa uma tabela de distribuição de frequências usando 7 classes indicando frequências absolutas, frequências relativas, frequências absolutas acumuladas, frequências relativas acumuladas.
(b) Faça um histograma e comente a distribuição dos dados.
(c) Calcule a média, a mediana, a variância e o desvio padrão dos dados
com base na tabela montada no item (a). Esses valores são exatos
ou aproximados? Explique sua resposta.
(d) Identique a classe modal.

'''

import matplotlib.pyplot as plt
import pandas as pd
import Dispersao
import Centralidade


def reparte_lista(freq, n):
    for i in range(0, len(freq), n):
        yield freq[i:i + n]


if __name__ == '__main__':

    arq_name = "frequenciasAEDestresse.txt"
    frequencias = []

    '''
    ITEM A)
    '''
    # primeiro vamos adicionar os dados do arquivo numa lista
    with open(arq_name, "r") as arq:
        frequencias = [linha.strip() for linha in arq]

    '''
    o erro está aqui, tenho q mudar o critério de repartição, desse jeito não me diz nada sobre meus dados
    '''

    # ordenando de forma crescente podemos dividir nossos dados em grupos
    frequencias = sorted(frequencias)
    dados_estresse = [1.43, 1.48 - 1.54, 1.55 - 1.61, 1.62 - 1.68, 1.69 - .1.75, 1.76 - 1.82, 1.83 - 1.89]
    for dado in frequencias:
        if int(dado) <= dados_estresse[len(dado)] & & int(dado) > dados_estresse[len(dado) - 1]:
            classes_estresse[dado] + +

    # n_classes = 7
    # classes_estresse = list(reparte_lista(frequencias, n_classes))
    # print(classes_estresse)

    # agora vamos reunir esses grupos numa lista ordenada
    ordem_estresse = ["{}-{}".format(classe[0], classe[-1]) for classe in classes_estresse]

    # frequencias absolutas por classe
    freq_absoluta = [len(classe) for classe in classes_estresse]

    # frequencias relativas por classe
    freq_relativa = [(len(classe) * 100) / len(classes_estresse) for classe in classes_estresse]

    # frequencias absolutas acumuladas por classe
    freq_abs_acumulada = [len(classe) if len(classe) == 0 else len(classe) + (len(classe) - 1) for classe in classes_estresse]

    # frequencias relativas acumuladas por classe
    freq_rel_acumulada = [((len(classe) + (len(classe) - 1)) * 100) / len(classes_estresse) for classe in classes_estresse if len(classe) > 0]

    # vamos organizar nossos dados numa tabela
    frequencias = []
    for i in range(len(freq_absoluta)):
        frequencias = frequencias.append([(freq_absoluta[i]), (freq_relativa[i]), (freq_abs_acumulada[i]), (freq_rel_acumulada[i])])

    tabela_absoluta = pd.DataFrame(frequencias, columns=['Frequência Absoluta', 'Frequência Relativa', 'Frequência Absoluta Acumulada', 'Frequência Relativa Acumulada'], index=ordem_estresse)
    tabela_absoluta.head()

    '''
    ITEM B)
    '''
