#solução 2
def tem_duplicados(lista):
    lista_ordenada = sorted(lista)
    for i in range(len(lista_ordenada) - 1):
        if lista_ordenada[i] == lista_ordenada [i+1]:
            return True
    return False