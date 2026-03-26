# 35. Desenvolva um algoritmo que peça ao usuário para digitar dois números e verifique se a multiplicação deles é igual a 20.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número:"))

multiplicacao = numero1 * numero2

if multiplicacao == 20:
    print("A multiplicação dos dois números é igual a 20.")
else:
    print("A multiplicação dos dois números é igual a outro valor diferente de 20.")