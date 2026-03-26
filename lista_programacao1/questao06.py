# 6. Desenvolva um programa que pergunte ao usuário uma operação matemática (+, -, *, /) e dois números, e realize a operação escolhida.
operacao = input("Digite a operação desejada (+, -, *, /): ")
numero = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))

soma = numero + numero2
sub = numero - numero2
mult = numero * numero2
div = numero / numero2

if operacao == "+":
    print(f"A soma é {soma}")
elif operacao == "-":
    print(f"A subtração é {sub}")
elif operacao == "*":
    print(f"A multiplicação é {mult}")
elif operacao == "/":
    print(f"A divisão é {div}")
else:
    print("Operação inválida.")