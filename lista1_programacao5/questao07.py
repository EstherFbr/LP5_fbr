# 7. Escreva um programa que peça ao usuário uma nota de 0 a 10 e classifique a nota como "Baixa", "Média" ou "Alta" usando estrutura condicional if.
nota = float(input("Digite a nota do aluno: "))

if nota < 5:
    print("Nota baixa.")
elif nota >= 5 and nota < 7:
    print("Nota médiana.")
elif nota >= 7 and nota <= 10:
    print("Nota alta.")
else:
    print("Nota inválida. Digite um valor entre 0 e 10.")