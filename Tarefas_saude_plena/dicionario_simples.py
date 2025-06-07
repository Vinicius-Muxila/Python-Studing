# dicionario com algumas tarefas

tarefas = {
    "correr" : ["2x na semana" , "Periodo de 1 mês"],
    "caminhar" : ["3x na semana" , "Periodo de 2 meses"],
    "beber agua" : ["2 litros e meio por dia" , "Durante 3 semanas"]
}

# acrescentar uma nova tarefa

tarefas["pedalar"] = ["3x na semana" , "Periodo de 2 meses"]

# pesquisar todas as tarefas inseridas

for tarefa in tarefas:
    print(tarefa)

# exlcluir uma tarefa

tarefas.pop("pedalar")
print(tarefas)

# verificar se uma tarefa existe

if "pedalar" in tarefas:
    print("Esta tarefa existe.")
else:
    print("Esta tarefa não existe")

