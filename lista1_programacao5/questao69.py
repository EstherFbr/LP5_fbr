# 69. Crie no algoritmo 67 as seguintes funcionalidades:
# Informe ao usuário em caso de empate.
# Crie uma forma de não permitir que um jogador jogue no mesmo lugar que já tenha uma jogada realizada.
# Atualmente o jogo encerra com o vencedor, ele agora também deve encerrar em caso de empate.
# Ao finalizar o jogo deve ser informado ao usuário uma mensagem solicitando uma nova partida, o sistema de reiniciar o jogo em caso de sim, e encerrar o programa em caso de não.
# Refatore a funcionalidade que verifica a vitoria e pense em uma forma de simplificar o código corrigido.

def mostrar_tabuleiro(tab):
    print()
    print(f" {tab[0]} | {tab[1]} | {tab[2]} ")
    print("---+---+---")
    print(f" {tab[3]} | {tab[4]} | {tab[5]} ")
    print("---+---+---")
    print(f" {tab[6]} | {tab[7]} | {tab[8]} ")
    print()


def verificar_vitoria(tab, jogador):
    combinacoes = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    
    return any(tab[a] == tab[b] == tab[c] == jogador for a,b,c in combinacoes)


def jogo():
    tabuleiro = [" "] * 9
    jogador_atual = "X"

    while True:
        mostrar_tabuleiro(tabuleiro)

        try:
            jogada = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")) - 1

            if jogada < 0 or jogada > 8:
                print("Posição inválida!")
                continue

            if tabuleiro[jogada] != " ":
                print("Posição já ocupada!")
                continue

            tabuleiro[jogada] = jogador_atual

            # verifica vitória
            if verificar_vitoria(tabuleiro, jogador_atual):
                mostrar_tabuleiro(tabuleiro)
                print(f"Jogador {jogador_atual} venceu! Parabéns!")
                break

            # verifica empate
            if " " not in tabuleiro:
                mostrar_tabuleiro(tabuleiro)
                print("Deu empate!")
                break

            # troca jogador
            jogador_atual = "O" if jogador_atual == "X" else "X"

        except ValueError:
            print("Digite um número válido!")


def jogo_da_velha():
    while True:
        jogo()

        opcao = input("Deseja jogar novamente? (s/n): ").lower()
        if opcao != "s":
            print("Obrigado por jogar, volte mais vezes!")
            break

jogo_da_velha()