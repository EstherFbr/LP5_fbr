# 43. Desenvolva um programa que pergunte ao usuário quantas vezes ele quer que uma mensagem seja exibida, e depois use um for para imprimir essa mensagem repetidas vezes.
mensagem = input("Digite a mensagem que deseja exibir: ")
vezes = int(input("Quantas vezes a mensagem deve ser exibida? "))


for i in range(vezes):
    print(mensagem)
