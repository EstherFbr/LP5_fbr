# 1. Crie um programa que pergunte ao usuário um número de 1 a 3 e exiba o nome correspondente ao número (1: "um", 2: "dois", 3: "três").
print('1')
print('2')
print('3')


opcao = int(input('Escolha um número de 1 a 3: '))

match opcao:
    case 1:
        print('Você escolheu 1')
    case 2:
        print('Você escolheu 2')
    case 3:
        print('Você escolheu 3')
    case _:
        print('Opção inválida. Escolha um número de 1 a 3.')