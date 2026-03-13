# Condiconal if
# acompanhada = 'Sim'
# idade = 15

# if idade >=18:
#     print('Você pode assistir ao filme')
# elif (idade >=15 and <=17) and acompanhada == 'Sim'
#     print('Você pode assistir o filme')
# else:
#     print('Você não pode assistir o filme')

print('0 - cadastrar')
print('1 - editar')
print('2 - exluir')

opcao = int(input('O que deseja realizar? '))

match opcao:
    case 0:
        print('Você escolheu cadastrar')
    case 1:
        print('Você escolheu editar')
    case 2:
        print('Você escolheu excluir')
    case _:
        print('Opção inválida')