def contar_pedidos_pares(pilha_de_pedidos):
    return sum(1 for pedido in pilha_de_pedidos if pedido % 2 == 0)


if __name__ == "__main__":
    pilha_de_pedidos = [101, 202, 303, 404, 505, 606, 707]
    print("Quantidade de pedidos pares:", contar_pedidos_pares(pilha_de_pedidos))
