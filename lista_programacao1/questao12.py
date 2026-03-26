# 12. Escreva um programa que peça ao usuário para escolher um modo de transporte (carro, bicicleta, a pé) e exiba uma mensagem com a velocidade média correspondente.
transporte = input("Digite um modo de transporte (carro, bicicleta, ônibus, trem, a pé): ")
if transporte == "carro":
    print("Velocidade média: 60 km/h")
elif transporte == "bicicleta":
    print("Velocidade média: 15 km/h")
elif transporte == "ônibus":
    print("Velocidade média: 40 km/h")
elif transporte == "trem":
    print("Velocidade média: 80 km/h")
elif transporte == "a pé":
    print("Velocidade média: 5 km/h")
else:
    print("Meio de transporte desconhecido.")