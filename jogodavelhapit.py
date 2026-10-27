# ==========================================
# JOGO DA VELHA - FACULDADE PIT
# Logica, Algoritmos e Programacao
# Anna Luiza e Cristhian Mesquita
# ==========================================



def criar_tabuleiro(tamanho):
    tabuleiro = []

    for i in range(tamanho):
        linha = []

        for j in range(tamanho):
            linha.append(" ")

        tabuleiro.append(linha)

    return tabuleiro



def mostrar_tabuleiro(tabuleiro, tamanho):
    print("\n     1   2   3")

    for i in range(tamanho):
        print("   +---+---+---+")

        print(" " + str(i + 1) + " |", end=" ")

        for j in range(tamanho):
            if tabuleiro[i][j] == " ":
                print(str(i * tamanho + j + 1), end=" | ")
            else:
                print(tabuleiro[i][j], end=" | ")

        print()

    print("   +---+---+---+\n")
