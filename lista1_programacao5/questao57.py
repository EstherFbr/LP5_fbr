# 57. Crie um programa que peça ao usuário para adivinhar um número secreto entre 1 e 10. Continue pedindo até que ele adivinhe o número corretamente.
import random
numero_secreto = random.randint(1, 10)


while True:
    palpite = int(input("Adivinhe o número secreto entre 1 e 10: "))
    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    else:
        print("Você errou. Tente novamente.")