from Tarefas_saude_plena.funcoes_tarefas import *

tarefas = {}
opcao = perguntar ()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "D":
    if opcao == "I":
        inserir(tarefas)

    opcao = perguntar ()
    if opcao == "P":
        pesquisar=input("Digite o nome da tarefa que deseja pesquisar: ")
        for elemento in tarefas:
            if pesquisar==elemento["tarefa"]:
                print("Frequência..: ", elemento["frequencia"])
                print("Tempo..:", elemento["tempo"])
        
