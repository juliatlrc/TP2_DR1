def contar_pedidos_impares(pilha_de_pedidos):
    return sum(1 for pedido in pilha_de_pedidos if pedido % 2 != 0)


if __name__ == "__main__":
    pilha_de_pedidos = [10,11,12,13,14,15,16]
    print("Quantidade de pedidos ímpares:", contar_pedidos_impares(pilha_de_pedidos))
