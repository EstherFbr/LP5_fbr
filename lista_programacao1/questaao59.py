# 59. Escreva um programa que solicite ao usuário para digitar dois números e verifique se o primeiro é maior que o segundo. Continue pedindo números até que o primeiro número seja maior que o segundo.
while True:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    
    if numero1 > numero2:
        print(f"O primeiro número ({numero1}) é maior que o segundo número ({numero2}).")
        break
    else:
        print(f"O primeiro número ({numero1}) é menor que o segundo número ({numero2}). Tente novamente.")