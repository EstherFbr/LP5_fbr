# 49. Desenvolva um programa que peça ao usuário para inserir 7 números e, ao final, exiba quantos desses números são maiores que 10.
contador_maiores_que_10 = 0


for i in range(7):
    numero = float(input(f"Digite o número {i + 1}: "))
    if numero > 10:
        contador_maiores_que_10 += 1
print(f"Quantidade de números maiores que 10: {contador_maiores_que_10}")
