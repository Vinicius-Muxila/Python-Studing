def perguntar ():
    return input("O que deseja realizar?\n"+
                 "<I> - Para inserir uma nova tarefa.\n"+
                 "<P> - Para pesquisar uma tarefa.\n"+
                 "<E> - Para editar uma tarefa.\n"+
                 "<D> - Para deletar uma tarefa.").upper()

def inserir (dicionario):
    dicionario[input("Digite o nome da tarefa: ").upper()]=[input("Digite a frequencia da tarefa: ")],
    [input("Digite por quantos minutos esta tarefa deverá ser realizada: ")]


