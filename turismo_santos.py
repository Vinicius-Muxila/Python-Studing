restaurante = {"Churrascaria":"Churrascaria Tertúlia - Av. Bartholomeu de Gusmão, 187 - Ponta da Praia",
             "Frutos do Mar":"Terraço Restaurante - Alameda Ari Barroso, 274 - Ilha Porchat",
             "Picanha na Brasa":"Manolinho Bar - Vila Sao Jorge, São Vicente"}

passeio = {"Aquário":"Aquário de Santos - Av. Bartholomeu de Gusmão, s/nº - Ponta da Praia",
         "Museu":"Museu do café - R. Quinze de Novembro, 95 - Centro",
         "Passeio de barco":"Passeio de barco para o Forte - Ponte Edgard Perdigão na Ponta da Praia"}

opcao = input("O que deseja fazer hoje, Gabriel? Digite:\n"+
            "1 - Se desejar ir a um RESTAURANTE.\n"+
            "2 - Se deseja buscar por um PASSEIO.\n"+
            "Resposta: ")

if opcao == "1":

  escolha_restaurante = input("Temos algumas opções,\n"+ 
            "e para saber o endereço, digite: \n"+
            "1 - Caso prefira ir em uma CHURRASCARIA\n"+
            "2 - Se a opção for comer FRUTOS DO MAR\n"+
            "3 - Se pretende comer uma PICANHA NA BRASA\n"+
            "Resposta: ")

  if escolha_restaurante == "1":
    print("Sua escolha foi comer diversos cortes das melhores carnes na " + restaurante["Churrascaria"])

  elif escolha_restaurante == "2":
    print("Sua escolha foi se deliciar comendo frutos do mar no " + restaurante["Frutos do Mar"])

  elif escolha_restaurante == "3":
    print("Sua escolha foi comer uma deliciosa Picanha na Brasa no " + restaurante["Picanha na Brasa"])

  else:
    ("Digite uma opção válida.")

elif opcao == "2":

  escolha_passeio = input("Temos algumas opções,\n"+ 
            "e para saber onde ir, digite: \n"+
            "1 - AQUARIO\n"+
            "2 - MUSEU\n"+
            "3 - PASSEIO DE BARCO\n"+
            "Resposta: ")

  if escolha_passeio == "1":
    print("Se divirta vendo espécies distintas de animais no " + passeio["Aquário"])

  elif escolha_passeio == "2":
    print("Sua escolha foi conhecer sobre a história da segunda bebida mais consumida do mundo no " + passeio["Museu"])

  elif escolha_passeio == "3":
    print("Sua escolha foi se aventurar em um delicioso passeio de barco indo até " + passeio["Passeio de barco"])

  else:
    ("Digite uma opção válida.")

else:
  print("você não escolheu como opção 1-Restaurante ou 2-Passeio.")