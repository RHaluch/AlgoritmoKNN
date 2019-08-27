import Calculos, Classificar, MatrizConfusao

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
# print(matriz)
# Imprime o tamanho da matriz
# print(len(matriz))
# imprime a primeira linha da matriz
# print(matriz[0])
# imprime a classe da amostra
# print(matriz[0][4])

# preencher matriz treino
treino = []
for i in range(0, 35):
    treino.append(matriz[i])

for i in range(50, 85):
    treino.append(matriz[i])

for i in range(100, 135):
    treino.append(matriz[i])

# preecher matriz teste
teste = []
for i in range(35, 50):
    teste.append(matriz[i])

for i in range(85, 100):
    teste.append(matriz[i])

for i in range(135, 150):
    teste.append(matriz[i])

# valor de K
# k=int(input("Informe o K: "))
k = 21

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

print(classManhattan)
print(classEuclidiana)

matrizManhattan=MatrizConfusao.preencherMatriz(teste, classManhattan)
matrizEuclidiana=MatrizConfusao.preencherMatriz(teste, classEuclidiana)

print("matriz manhattan")
print(matrizManhattan[0])
print(matrizManhattan[1])
print(matrizManhattan[2])
print("matriz euclidiana")
print(matrizEuclidiana[0])
print(matrizEuclidiana[1])
print(matrizEuclidiana[2])

print(44/45)
