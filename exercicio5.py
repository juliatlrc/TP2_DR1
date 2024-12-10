def tarefa_no_topo(pilha_de_tarefas):
    return pilha_de_tarefas[-1] if pilha_de_tarefas else None

if __name__ == "__main__":
    pilha_de_tarefas = ["Tarefa 1", "Tarefa 2", "Tarefa 3", "Tarefa 4"]
    print("Tarefa no topo:", tarefa_no_topo(pilha_de_tarefas))
    pilha_de_tarefas.append("Tarefa 5")
    print("Tarefa no topo:", tarefa_no_topo(pilha_de_tarefas))
    pilha_de_tarefas.pop()
    print("Tarefa no topo:", tarefa_no_topo(pilha_de_tarefas))
