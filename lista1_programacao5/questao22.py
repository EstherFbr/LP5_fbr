# 22. Escreva um programa que peça ao usuário para inserir dois números e verifique se o primeiro é maior que o segundo.
numero1 = int(input('Digite o primeiro número:'))
numero2 = int(input('Digite o segundo número:'))

if numero1 > numero2:
    print(f'{numero1} é maior que {numero2}.')
else:
    print(f'{numero1} não é maior que {numero2}.')