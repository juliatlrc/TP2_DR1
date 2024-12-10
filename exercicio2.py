def ordenar_registros(arr):
    if len(arr) <= 1:
        return arr

    aux = arr[:]
    _sort(arr, aux, 0, len(arr) - 1)
    return arr


def _sort(arr, aux, inicio, fim):
    if inicio >= fim:
        return

    meio = (inicio + fim) // 2

    _sort(arr, aux, inicio, meio)
    _sort(arr, aux, meio + 1, fim)

    if arr[meio] <= arr[meio + 1]:
        return

    _merge(arr, aux, inicio, meio, fim)


def _merge(arr, aux, inicio, meio, fim):
    for k in range(inicio, fim + 1):
        aux[k] = arr[k]

    i = inicio
    j = meio + 1
    k = inicio

    while i <= meio and j <= fim:
        if aux[i] <= aux[j]:
            arr[k] = aux[i]
            i += 1
        else:
            arr[k] = aux[j]
            j += 1
        k += 1

    while i <= meio:
        arr[k] = aux[i]
        i += 1
        k += 1


if __name__ == "__main__":
    v = [-1, 7, -3, 11, 4, -2, 4, 8]
    ordenar_registros(v)
    print("Resultado:", v)
