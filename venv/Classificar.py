def classificar(lista):
    if(lista.count(0)>lista.count(1) and lista.count(0)>lista.count(2)
    and lista.count(0)>lista.count(3)):
        return 0;
    elif(lista.count(1)>lista.count(2)):
        return 1;
    else:
        return 2;
