# 40. Escreva um programa que peça ao usuário para inserir três números e verifique se todos são iguais.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))


if numero1 == numero2 == numero3:
    print("Todos os números são iguais.")
elif numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
    print("Pelo menos dois números são iguais.")
else:
    print("Todos os números são diferentes.")
    