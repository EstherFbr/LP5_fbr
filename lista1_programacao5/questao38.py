# 38. Escreva um programa que peça ao usuário para digitar sua altura em metros e verifique se ela é maior que 1.75.
altura = float(input("Digite sua altura em metros: "))


if altura > 1.75:
    print("Sua altura é maior que 1.75 metros.")
elif altura == 1.75:
    print("Sua altura é exatamente 1.75 metros.")
else:
    print("Sua altura é menor que 1.75 metros.")
