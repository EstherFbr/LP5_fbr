# 21. Escreva um algoritmo que peça ao usuário para digitar um número e verifique se ele é maior, menor ou igual a 10.
numero = float(input("Digite um número: "))

if numero < 10:
    print("O número é menor que 10.")
elif numero == 10:
    print ("O número é igual a 10.")
else:
    print("O número é maior que 10.")