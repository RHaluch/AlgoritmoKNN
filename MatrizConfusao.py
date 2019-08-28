def preencherMatriz(amostra, listaClass):
    matriz = []
    for i in range(0, 3):
        matriz.append([0] * 3)

    for i in range(0, 15):
        if amostra[i][4] == int(listaClass[i][1]):
            matriz[0][0] += 1
        elif (int(listaClass[i][1]) == 1):
            matriz[0][1] += 1
        else:
            matriz[0][2] += 1

    for i in range(15, 30):
        if amostra[i][4] == int(listaClass[i][1]):
            matriz[1][1] += 1
        elif (int(listaClass[i][1]) == 0):
            matriz[1][0] += 1
        else:
            matriz[1][2] += 1

    for i in range(30, 45):
        if amostra[i][4] == int(listaClass[i][1]):
            matriz[2][2] += 1
        elif (int(listaClass[i][1]) == 1):
            matriz[2][1] += 1
        else:
            matriz[2][0] += 1

    return matriz
