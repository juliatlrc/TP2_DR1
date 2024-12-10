class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def _hash(self, chave):
        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):
        indice = self._hash(chave)
        for item in self.tabela[indice]:
            if item[0] == chave:
                item[1] = valor
                return
        self.tabela[indice].append([chave, valor])

    def buscar(self, chave):
        indice = self._hash(chave)
        for item in self.tabela[indice]:
            if item[0] == chave:
                return item[1]
        return None

    def remover(self, chave):
        indice = self._hash(chave)
        for item in self.tabela[indice]:
            if item[0] == chave:
                self.tabela[indice].remove(item)
                return True
        return False


if __name__ == "__main__":
    tabela = TabelaHash(10)
    tabela.inserir("chave1", "valor1")
    tabela.inserir("chave2", "valor2")
    tabela.inserir("chave3", "valor3")

    print("Valor associado a 'chave1':", tabela.buscar("chave1"))
    print("Valor associado a 'chave2':", tabela.buscar("chave2"))

    tabela.remover("chave1")
    print("Valor associado a 'chave1' após remoção:", tabela.buscar("chave1"))

    tabela.inserir("chave2", "novo_valor2")
    print("Valor atualizado associado a 'chave2':", tabela.buscar("chave2"))
