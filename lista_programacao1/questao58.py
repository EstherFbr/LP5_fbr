# 58. Desenvolva um algoritmo que solicite ao usuário uma palavra e continue pedindo outra palavra até que ele digite "sair".
while True:
    palavra = input("Digite uma palavra (ou 'sair' para encerrar): ")
    if palavra.lower() == "sair":
        print("Encerrando o programa.")
        break
    else:
        print(f"Palavra digitada: {palavra}")