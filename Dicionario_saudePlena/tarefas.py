from funcoes import *

tarefas = {}
opcao = perguntar()

while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="D":
  if opcao == "I":
    inserir(tarefas)

    opcao = perguntar()
    
if opcao == "P":
    pesquisar(tarefas)

    opcao = perguntar()
      
if opcao == "E":
    editar(tarefas)

    opcao = perguntar()
        
if opcao == "D":
    deletar(tarefas)

    opcao = perguntarSair()

print("Programa encerrado.")