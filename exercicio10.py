def contar_livros_impares(fila_de_livros):
    contador = 0
    for livro in fila_de_livros:
        if livro % 2 != 0:
            contador += 1
    return contador

if __name__ == "__main__":
    fila_de_livros = [10,12,13,14,15,16]
    print("Quantidade de livros com números ímpares:", contar_livros_impares(fila_de_livros))
