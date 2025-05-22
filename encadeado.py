nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
bebado = input("Digite SIM ou NÃO se consumiu bebida alcoolica: ").upper()

if idade >= 18:
    print("Você pode continuar a dirigir.")
elif bebado == "SIM":
    print("Você não devia estar dirigindo, então está preso!")
else:
    print("Você não tem permissão de dirigir. Preciso que chame um responsável.")