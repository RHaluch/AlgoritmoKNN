import math

def ordenar(lista):
    for i in range(0,lista.__len__()-1):
        for j in range(i+1,lista.__len__()):
            if lista[j][0]<lista[i][0]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux
    return lista

def manhattan(amostra, treino):
    distancias=[]
    for i in range(0,105):
        distancia=abs(amostra[0]-treino[i][0])+\
                  abs(amostra[1]-treino[i][1])+\
                  abs(amostra[2]-treino[i][2])+\
                  abs(amostra[3]-treino[i][3])

        #distancia=float("{:.2f}".format(distancia))
        distancias.append([distancia,treino[i][4]])

    distancias=ordenar(distancias)
    return distancias

def euclidiana(amostra, treino):
    distancias=[]
    for i in range(0,105):
        distancia=((abs(amostra[0]-treino[i][0]))**2)+\
                  ((abs(amostra[1]-treino[i][1]))**2)+\
                  ((abs(amostra[2]-treino[i][2]))**2)+\
                  ((abs(amostra[3]-treino[i][3]))**2)
        distancia=math.sqrt(distancia)
        #distancia = float("{:.2f}".format(distancia))
        distancias.append([distancia, treino[i][4]])

    distancias=ordenar(distancias)
    return distancias