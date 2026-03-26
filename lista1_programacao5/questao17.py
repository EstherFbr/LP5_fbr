# 17. Crie um programa que solicite ao usuário dois números e exiba a soma, subtração, multiplicação e divisão entre eles.
if(input("Deseja realizar uma operação matemática? (S/N): ") ):
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    soma = numero1 + numero2
    sub = numero1 - numero2
    mult = numero1 * numero2
    div = numero1 / numero2

    print(f'A soma é {soma}')
    print(f'A sub é {sub}')
    print(f'A mult é {mult}')
    print(f'A div é {div}')