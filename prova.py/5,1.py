#solução 1
def tem_duplicados(lista):
    for i in range (len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False