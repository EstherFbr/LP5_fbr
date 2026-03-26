# 26. Desenvolva um algoritmo que peça ao usuário para inserir dois números e verifique se ambos são múltiplos de 5.
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))


if numero1 % 5 == 0 and numero2 % 5 == 0:
    print("Ambos os números são múltiplos de 5.")
else:
    print("Pelo menos um dos números não é múltiplo de 5.")
