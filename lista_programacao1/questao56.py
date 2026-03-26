# 56. Escreva um programa que pergunte ao usuário quantas vezes ele quer que uma mensagem seja exibida, e utilize um laço while para exibir a mensagem a quantidade de vezes desejada.
quantidade = int(input("Quantas vezes deve-se exibir a mensagem? "))
contador = 0

while contador < quantidade:
    print("Boa aula de programação!")
    contador += 1
