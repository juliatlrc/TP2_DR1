def encontrar_duplicados_bruto(lista):
    duplicados = set()
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                duplicados.add(lista[i])
    return list(duplicados)


def encontrar_duplicados_rapido(lista):
    vistos, duplicados = set(), set()
    for num in lista:
        if num in vistos:
            duplicados.add(num)
        vistos.add(num)
    return list(duplicados)


if __name__ == "__main__":
    lista = [5, 1, 2, 3, 4, 1, 5, 6, 7, 3, 8, 9, 2, 10]
    print("Força bruta:", encontrar_duplicados_bruto(lista))
    print("Estrutura eficiente:", encontrar_duplicados_rapido(lista))
