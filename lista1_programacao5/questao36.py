# 36. Crie um programa que solicite ao usuário um número de 1 a 12 e exiba o mês correspondente.
mes = int(input("Digite um número de 1 a 12 para escolher um mês: "))

if mes == 1:
    mês = "Janeiro"
elif mes == 2:
    mês = "Fevereiro"
elif mes == 3:
    mês = "Março"
elif mes == 4:
    mês = "Abril"
elif mes == 5:
    mês = "Maio"
elif mes == 6:
    mês = "Junho"
elif mes == 7:
    mês = "Julho"
elif mes == 8:
    mês = "Agosto"
elif mes == 9:
    mês = "Setembro"
elif mes == 10:
    mês = "Outubro"
elif mes == 11:
    mês = "Novembro"
elif mes == 12:
    mês = "Dezembro"

else:
    print("Número inválido. Por favor, digite um número de 1 a 12.")

print(f"O mês correspondente ao número {mes} é: {mês}.")
