# 8. Desenvolva um algoritmo que pergunte ao usuário o estado civil (solteiro, casado, divorciado, viúvo) e exiba uma mensagem correspondente.
estado = str(input("Digite o seu estado cívil solteiro, casado, divorciado ou viúvo: "))

if estado == "solteiro":
    print("Você está solteiro.")
if estado == "casado":
    print("ParaVocê é casado!")
if estado == "divorciado":
    print("VOcê é divorciado.")
if estado == "viúvo" or estado == "viuvo":
    print("Você é viúvo.")
else:   
    print("Estado civil inválido.")






