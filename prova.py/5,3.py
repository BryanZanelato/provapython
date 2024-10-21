#solução 3
def tem_duplicados(lista):
    elementos_vistos = set()
    for elemento in lista:
        if elemento in elementos_vistos:
            return True
        elementos_vistos.add(elemento)
    return False