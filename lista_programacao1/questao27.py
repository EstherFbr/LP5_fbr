# 27. Crie um programa que solicite ao usuário três números e exiba o maior deles.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))


if numero2 > numero1 and numero2 > numero3:
    print("O maior número é: ", numero2)
elif numero3 > numero1 and numero3 > numero2:
    print("O maior número é: ", numero3)
else:
    print("O maior número é: ", numero1)