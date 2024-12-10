def ordenar_fila(fila):
    for i in range(len(fila)):
        for j in range(0, len(fila) - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila


if __name__ == "__main__":
    fila = [34, 7, 23, 32, 5, 62]
    print("Fila original:", fila)
    fila_ordenada = ordenar_fila(fila)
    print("Fila ordenada:", fila_ordenada)
