class FilaAtendimento:
    def __init__(self):
        self.fila = []

    def adicionar_cliente(self, nome):
        self.fila.append(nome)

    def atender_cliente(self):
        if self.fila:
            return self.fila.pop(0)
        return "Nenhum cliente na fila."

    def tamanho_fila(self):
        return len(self.fila)


if __name__ == "__main__":
    fila = FilaAtendimento()
    fila.adicionar_cliente("Cliente 1")
    fila.adicionar_cliente("Cliente 2")
    fila.adicionar_cliente("Cliente 3")

    print("Atendendo:", fila.atender_cliente())
    print("Clientes na fila:", fila.tamanho_fila())

    fila.adicionar_cliente("Cliente 4")
    print("Clientes na fila:", fila.tamanho_fila())

    print("Atendendo:", fila.atender_cliente())
    print("Atendendo:", fila.atender_cliente())
    print("Clientes na fila:", fila.tamanho_fila())
