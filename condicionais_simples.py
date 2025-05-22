nome = input("Digite seu nome: ")   
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("O aluno " + nome + " tem " + str(idade) + " anos e está apto a tirar sua habilitação.")
else:
    print("O aluno " + nome + " tem " + str(idade) + " anos e ainda não possui idade o suficente para dirigir.")