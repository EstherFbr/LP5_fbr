# 16. Desenvolva um programa que peça ao usuário um tipo de combustível (gasolina, etanol, diesel) e exiba o preço correspondente por litro.
combustivel = input("Digite o tipo de combustível que você deseja (Gasolina, Etanol ou Diesel): ")

etanol = 5.10
diesel = 7.50
gasolina = 6.51

if combustivel == "Etanol":
    print(f"O preço do etanol é R${etanol} por litro.")
elif combustivel == "Gasolina":
    print(f"O preço da gasolina é R${gasolina} por litro.")
elif combustivel == "Diesel":
    print(f"O preço do diesel é R${diesel} por litro.")
else:
    print("Tipo de combustível inválido.")