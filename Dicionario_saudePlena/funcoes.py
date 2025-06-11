def perguntar():
    return input("O que deseja realizar?\n"+
            "<I> - Para inserir uma nova tarefa.\n"+
            "<P> - Para pesquisar uma tarefa.\n"+
            "<E> - Para editar uma tarefa.\n"+
            "<D> - Para deletar uma tarefa.\n"+
            "Resposta: ").upper()

def perguntarSair():
    return input("O que deseja realizar?\n"+
            "<I> - Para inserir uma nova tarefa.\n"+
            "<P> - Para pesquisar uma tarefa.\n"+
            "<E> - Para editar uma tarefa.\n"+
            "<D> - Para deletar uma tarefa.\n"+
            "<S> - Para sair.\n"+
            "Resposta: ").upper()

def inserir(Dicionario):
    tarefa = input("Digite a tarefa que deseja inserir: ").upper()
    frequencia = input("Digite a frequencia desta tarefa: ").upper()
    periodo = input("Digite o perido desta tarefa: ").upper()
    Dicionario[tarefa] = [frequencia , periodo]


def pesquisar(Dicionario):
    pesquisar = input("Digite a tarefa que deseja pesquisar: ").upper()
    pesquisar = Dicionario[pesquisar]
    print(pesquisar)

def editar(Dicionario):
    tarefa = input("Digite qual tarefa deseja editar: ").upper()
    frequencia = input("Digite a frequencia desta tarefa: ").upper()
    periodo = input("Digite o perido desta tarefa: ").upper()
    Dicionario[tarefa] = [frequencia , periodo]
    print(Dicionario)

def deletar(Dicionario):
    deletar = input("Digite a tarefa que deseja excluir: ").upper()
    Dicionario.pop(deletar)
    print(Dicionario)