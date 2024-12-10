def ordenar_pilha(pilha):
    pilha_aux = []
    while pilha:
        temp = pilha.pop()
        while pilha_aux and pilha_aux[-1] > temp:
            pilha.append(pilha_aux.pop())
        pilha_aux.append(temp)
    return pilha_aux

if __name__ == "__main__":
    pilha = [10, 7.0, 9.5, 6.0, 9.0, 7.5]
    pilha_final = ordenar_pilha(pilha)
    print("Pilha ordenada:", pilha_final)
