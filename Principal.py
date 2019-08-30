import Calculos, Classificar, MatrizConfusao
import pandas as pd

# Muda o rótulo de uma classe para inteiro
def replace_label(classe):
    if 'Iris-setosa' in classe:
        return 0
    elif 'Iris-versicolor' in classe:
        return 1
    elif 'Iris-virginica' in classe:
        return 2

# Abre o arquivo
file = open("iris.data")

# Lê o arquivo e armazena em um vetor. Cada elemento do Vetor é uma linha.
linhas = file.readlines()

matriz = []

for linha in linhas:
    # Separa os dados em uma lista
    vetor = linha.split(',')
    for i in range(0, 4):
        # Converte os 4 primeiros elementos em float
        vetor[i] = float(vetor[i])
    # Muda o elemento 5 da matriz para um inteiro, que representa um rótulo
    vetor[4] = replace_label(vetor[4])
    # Adiciona a linha formatada na matriz
    matriz.append(vetor)

# Imprime a matriz completa
#print(matriz)
# Imprime o tamanho da matriz
#print(len(matriz))
# imprime a primeira linha da matriz
#print(matriz[0])
# imprime a classe da amostra
#print(matriz[0][4])

# preencher matriz treino
treino = []
for i in range(15, 50):
    treino.append(matriz[i])

for i in range(65, 100):
    treino.append(matriz[i])

for i in range(115, 150):
    treino.append(matriz[i])
#print(treino)
#print(treino.__len__())

# preecher matriz teste
teste = []
for i in range(0, 15):
    teste.append(matriz[i])

for i in range(50, 65):
    teste.append(matriz[i])

for i in range(100, 115):
    teste.append(matriz[i])

# valor de K
k=int(input("Informe o K: "))
#k = 21

calcManhattan = []
calcEuclidiana = []
vizinhosManhattan = []
vizinhosEuclidiana = []
classManhattan = []
classEuclidiana = []
aux = []

# chamar calculos e armazenar k vizinhos
for i in range(0, 45):
    calcManhattan = Calculos.manhattan(teste[i], treino)
    for j in range(0, k):
        aux.append(calcManhattan[j][1])
    vizinhosManhattan.append(aux)
    aux = []

    calcEuclidiana = Calculos.euclidiana(teste[i], treino)
    for j in range(0, k):
        aux.append(calcEuclidiana[j][1])
    vizinhosEuclidiana.append(aux)
    aux = []

    # classificar cada amostra
    classManhattan.append([str(i + 1) + ' amostra ' + str(teste[i])
                           + ' Voto: ', str(Classificar.classificar(vizinhosManhattan[i]))])
    classEuclidiana.append([str(i + 1) + ' amostra ' + str(teste[i])
                            + ' Voto: ', str(Classificar.classificar(vizinhosEuclidiana[i]))])

print("\nClassificação Manhattan: "+str(classManhattan))
print("\nClassificação Euclidiana: "+str(classEuclidiana))


matrizManhattan= MatrizConfusao.preencherMatriz(teste, classManhattan)
matrizEuclidiana= MatrizConfusao.preencherMatriz(teste, classEuclidiana)

taxaAcerto = ((matrizManhattan[0][0]+matrizManhattan[1][1]+matrizManhattan[2][2])/teste.__len__())*100

#coisas novas PANDAS Series
indices=['Setosa','Versicolor','Virginica']
matrizManhattan = pd.DataFrame(matrizManhattan, index=indices, columns=indices)


#mostrar matrizes e taxas de acerto

print('\n------------------------------------------\n\nMatriz de confusão - Manhattan\n')
print(matrizManhattan)
print('\nTaxa de acerto = '+str(float("{:.2f}".format(taxaAcerto)))+' %')


taxaAcerto = ((matrizEuclidiana[0][0]+matrizEuclidiana[1][1]+matrizEuclidiana[2][2])/teste.__len__())*100
matrizEuclidiana = pd.DataFrame(matrizEuclidiana, index=indices, columns=indices)
print("\n------------------------------------------\nMatriz de confusão - Euclidiana\n")
print(matrizEuclidiana)

print('\nTaxa de acerto = '+str(float("{:.2f}".format(taxaAcerto)))+' %')


