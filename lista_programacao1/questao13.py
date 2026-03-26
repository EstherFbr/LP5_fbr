# 13. Crie um algoritmo que solicite ao usuário um mês do ano (1 a 12) e exiba a estação do ano correspondente.
mes = int(input("Digite um mês do ano (1 a 12): "))
if mes in [12, 1, 2]:
    print("Estação do ano: Verão")
elif mes in [3, 4, 5]:
    print("Estação do ano: Outono")
elif mes in [6, 7, 8]:
    print("Estação do ano: Inverno")
elif mes in [9, 10, 11]:
    print("Estação do ano: Primavera")
else:
    print("Mês inválido. Por favor, digite um número entre 1 e 12.")