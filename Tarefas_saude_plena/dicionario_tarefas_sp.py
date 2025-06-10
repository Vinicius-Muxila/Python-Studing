tarefas = {}
opcao = input("O que deseja realizar?\n"+
            "<I> - Para inserir uma nova tarefa.\n"+
            "<P> - Para pesquisar uma tarefa.\n"+
            "<E> - Para editar uma tarefa.\n"+
            "<D> - Para deletar uma tarefa.").upper()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="D":
  if opcao == "I":
    tarefa = input("Digite a tarefa que deseja inserir: ").upper()
    frequencia = input("Digite a frequencia desta tarefa: ").upper()
    periodo = input("Digite o perido desta tarefa: ").upper()
    tarefas = {tarefa : [frequencia , periodo]}

    opcao = input("O que deseja realizar?\n"+
            "<I> - Para inserir uma nova tarefa.\n"+
            "<P> - Para pesquisar uma tarefa.\n"+
            "<E> - Para editar uma tarefa.\n"+
            "<D> - Para deletar uma tarefa.").upper()
    
    if opcao == "P":
      pesquisar = input("Digite a tarefa que deseja pesquisar: ").upper()
      tarefas.get(pesquisar)
      print(tarefas)

      opcao=input("O que deseja realizar?\n" +
            "<I> - Para inserir uma nova tarefa.\n"+
            "<P> - Para pesquisar uma tarefa.\n"+
            "<E> - Para editar uma tarefa.\n"+
            "<D> - Para deletar uma tarefa.").upper()
      
      if opcao == "E":
        tarefa = input("Digite qual tarefa deseja editar: ").upper()
        frequencia = input("Digite a frequencia desta tarefa: ").upper()
        periodo = input("Digite o perido desta tarefa: ").upper()
        tarefa = {tarefa : [frequencia , periodo]}
        print(tarefas)

        opcao=input("O que deseja realizar?\n" +
            "<I> - Para inserir uma nova tarefa.\n"+
            "<P> - Para pesquisar uma tarefa.\n"+
            "<E> - Para editar uma tarefa.\n"+
            "<D> - Para deletar uma tarefa.").upper()
        
        if opcao == "D":
          deletar = input("Digite a tarefa que deseja excluir: ").upper()
          tarefas.pop(deletar)
          print(tarefas)

         
