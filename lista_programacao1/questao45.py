# 45. Escreva um algoritmo que peça ao usuário para inserir 5 números e, ao final, exiba o maior número inserido.
maior_numero = None


for i in range(5):
    numero = int(input("Digite um número: "))
    if maior_numero is None or numero > maior_numero:
        maior_numero = numero
print("O maior número digitado é:", maior_numero)