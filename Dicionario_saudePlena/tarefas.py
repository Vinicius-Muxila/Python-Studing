from funcoes import *

tarefas = {}
opcao = perguntar()

while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="D":

# inserir novas tarefas

  if opcao == "I":
    inserir(tarefas)

    opcao = perguntar()

# pesquisar tarefas já incluídas    
    
  elif opcao == "P":
    pesquisar(tarefas)

    opcao = perguntar()

# editar alguma tarefa já inserida    
      
  elif opcao == "E":
    editar(tarefas)

    opcao = perguntar()

# excluir alguma tarefa que foi inserida
        
  elif opcao == "D":
    deletar(tarefas)

    opcao = perguntarSair()
else:
  print("Programa encerrado.")