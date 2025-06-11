tarefas = {}
opcao = input("O que deseja realizar?\n"+
            "<I> - Para inserir uma nova tarefa.\n"+
            "<P> - Para pesquisar uma tarefa.\n"+
            "<E> - Para editar uma tarefa.\n"+
            "<D> - Para deletar uma tarefa.\n"+
            "Resposta: ").upper()

while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="D":
  if opcao == "I":
    tarefa = input("Digite a tarefa que deseja inserir: ").upper()
    frequencia = input("Digite a frequencia desta tarefa: ").upper()
    periodo = input("Digite o perido desta tarefa: ").upper()
    tarefas[tarefa] = [frequencia , periodo]

    opcao = input("O que deseja realizar?\n"+
            "<I> - Para inserir uma nova tarefa.\n"+
            "<P> - Para pesquisar uma tarefa.\n"+
            "<E> - Para editar uma tarefa.\n"+
            "<D> - Para deletar uma tarefa.\n"+
            "Resposta: ").upper()
    
  elif opcao == "P":
    pesquisar = input("Digite a tarefa que deseja pesquisar: ").upper()
    pesquisar = tarefas[pesquisar]
    print(pesquisar)

    opcao = input("O que deseja realizar?\n"+
            "<I> - Para inserir uma nova tarefa.\n"+
            "<P> - Para pesquisar uma tarefa.\n"+
            "<E> - Para editar uma tarefa.\n"+
            "<D> - Para deletar uma tarefa.\n"+
            "Resposta: ").upper()
      
  elif opcao == "E":
    tarefa = input("Digite qual tarefa deseja editar: ").upper()
    frequencia = input("Digite a frequencia desta tarefa: ").upper()
    periodo = input("Digite o perido desta tarefa: ").upper()
    tarefas[tarefa] = [frequencia , periodo]
    print(tarefas)

    opcao = input("O que deseja realizar?\n"+
            "<I> - Para inserir uma nova tarefa.\n"+
            "<P> - Para pesquisar uma tarefa.\n"+
            "<E> - Para editar uma tarefa.\n"+
            "<D> - Para deletar uma tarefa.\n"+
            "Resposta: ").upper()
        
  elif opcao == "D":
    deletar = input("Digite a tarefa que deseja excluir: ").upper()
    tarefas.pop(deletar)
    print(tarefas)

    opcao = input("O que deseja realizar?\n"+
            "<I> - Para inserir uma nova tarefa.\n"+
            "<P> - Para pesquisar uma tarefa.\n"+
            "<E> - Para editar uma tarefa.\n"+
            "<D> - Para deletar uma tarefa.\n"+
            "<S> - Para sair.\n"+
            "Resposta: ").upper()

else:
    print("Programa encerrado")