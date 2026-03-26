# 3. Desenvolva um programa que pergunte ao usuário o dia da semana (número de 1 a 7) e exiba o nome do dia correspondente.

print('1 - domingo')
print('2 - segunda')
print('3 - terça')
print('4 - quarta')
print('5 - quinta')
print('6 - sexta')
print('7 - sábado')

dia = int(input("Escolha um número de 1 a 7: "))


match dia:
    case 1:
        print("Você escolheu Domingo!")
    case 2:
        print("Você escolheu Segunda!")
    case 3:
        print("Você escolheu Terça!")
    case 4:
        print("Você escolheu Quarta!")
    case 5:
        print("Você escolheu Quinta!")
    case 6:
        print("Você escolheu Sexta!")
    case 7:
        print("Você escolheu Sábado!")
    case _:
        print("Opção inválida. Por favor escolha um número entre 1 e 7.")