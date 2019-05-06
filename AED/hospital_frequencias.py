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
    # primeiro vamos adicionar os dados do arquivo numa lista
    with open(arq_name, "r") as arq:
        frequencias = [linha for linha in arq]

    # ordenando de forma crescente podemos dividir nossos dados em grupos
    frequencias = sorted(frequencias)
    n_classes = 7
    classes_estresse = reparte_lista(frequencias, n_classes)

    # agora vamos reunir esses grupos numa lista ordenada
    ordem_estresse = []
    ordem_estresse = [ordem_estresse.append("{}-{}". format(classe[0], classe[-1])) for classe in classes_estresse]

    # frequencias absolutas por classe
    freq_absoluta = [len(classe) for classe in classes_estresse]

    # frequencias relativas por classe
    freq_relativa = [(len(classe) * 100) / len(classes_estresse) for classe in classes_estresse]

    # frequencias absolutas acumuladas por classe
    freq_abs_acumulada = [len(classe) + len(classe - 1) for classe in classes_estresse if len(classe) > 0]

    # frequencias relativas acumuladas por classe
    freq_rel_acumulada = [((len(classe) + len(classe - 1)) * 100) / len(classes_estresse) for classe in classes_estresse if len(classe) > 0]

    # agora vamos organizar nossos dados numa tabela
    tabela_absoluta = pd.DataFrame({'Frequência Absoluta': freq_absoluta,
                                    'Frequência Relativa': freq_relativa,
                                    'Frequência Absoluta Acumulada': freq_abs_acumulada,
                                    'Frequência Relativa Acumulada': freq_rel_acumulada}, index=ordem_estresse)
