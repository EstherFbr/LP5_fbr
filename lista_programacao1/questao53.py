# 53. Escreva um programa que peça ao usuário um número e exiba a contagem regressiva desse número até 1.
numero = int(input("Digite um número para a contagem regressiva: "))


if numero < 1:
    print("Atenção: digite um número maior ou igual a 1.")
else:
    print("Contagem regressiva:")
    for i in range(numero, 0, -1):
        print(i)