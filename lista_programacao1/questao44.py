# 44. Crie um programa que peça ao usuário 10 números e exiba apenas os números pares.
numeros_pares = []


for i in range(10):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        numeros_pares.append(numero)

print("Números pares digitados:")
for numero in numeros_pares:
    print(numero)