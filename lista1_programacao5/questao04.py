# 4. Crie um algoritmo que solicite ao usuário uma cor (vermelho, verde, azul) e exiba uma mensagem correspondente à cor escolhida.
print("Vermelho")
print("Azul")
print("Verde")


cor = str(input("Escolha uma cor: "))


if cor == "Vermelho":
    print("Você escolheu Vermelho!")
elif cor == "Azul":
    print("Você escolheu Azul!")
elif cor == "Verde":
    print("Você escolheu Verde!")
else:
    print("Opção inválida. Por favor escolha uma das opcões.")