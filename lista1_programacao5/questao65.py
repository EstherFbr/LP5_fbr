# 65. Escreva um programa que solicite ao usuário uma lista de 5 números e exiba o maior e o menor número dessa lista.
numeros = []    

for i in range(5):
    numero = float(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

if numeros:
    numero_maior = max(numeros)
    numero_menor = min(numeros)
print(f"O maior número escolhido foi: {numero_maior}")
print(f"O menor número escolhido foi: {numero_menor}")