# 64. Crie uma lista com 10 números aleatórios e exiba apenas os números que são múltiplos de 3.
import random

numeros = [random.randint(1, 200) for _ in range(10)]
multiplos_de_3 = [num for num in numeros if num % 3 == 0]
print("Números gerados:", numeros)
print("Números que são múltiplos de 3 é:", multiplos_de_3)