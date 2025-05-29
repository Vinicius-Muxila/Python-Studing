
inventario=[]
resposta = "S"
while resposta == "S":
  equipamento={"equipamento":input("Seu equipamente é: "),"Valor":input("Digite o valor: "), "departamento":input("Digite o departamento: ")}
# #  equipamento=[input("Equipamento: "),
# #            float(input("Valor: ")),
#             int(input("Número Serial: ")),
#             input("Departamento: ")]
  inventario.append(equipamento)
  resposta = input("Digite \"S\" para continuar: ").upper()

for elemento in inventario:
  print("Nome: ", elemento["equipamento"])
  print("Valor: ", elemento["Valor"])
  print("departamento: ", elemento["departamento"])

busca=input("Digite o nome do equipamento que deseja buscar: ")
for elemento in inventario:
  if busca==elemento["equipamento"]:
    print("Valor..: ", elemento["Valor"])
    print("Depart..:", elemento["departamento"])

depreciacao=input("Digite o nome do equipamento que será depreciado: ")
for elemento in inventario:
  if depreciacao==elemento["tarefa"]:
    print("tarefa antiga: ", elemento["tarefa"])
    elemento["tarefa"] = input("Digite uma nova tarefa: ")
    print("Nova tarefa: ", elemento["tarefa"])

serial=int(input("Digite o serial do equipamento que será excluído: "))
for elemento in inventario:
  if elemento[2]==serial:
    inventario.remove(elemento)

for elemento in inventario:
  print("Nome.........: ", elemento[0])
  print("Valor........: ", elemento[1])
  print("Serial.......: ", elemento[2])
  print("Departamento.: ", elemento[3])


valores=[]
for elemento in inventario:
  valores.append(elemento[1])
if len(valores)>0:
  print("O equipamento mais caro custa: ", max(valores))
  print("O equipamento mais barato custa: ", min(valores))
  print("O total de equipamentos é de: ", sum(valores))