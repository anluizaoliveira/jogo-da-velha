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

def ler_numero(mensagem, minimo, maximo):
    while True:
        entrada = input(mensagem).strip()

        if entrada.isdigit():
            numero = int(entrada)

            if numero >= minimo and numero <= maximo:
                return numero

        print("Entrada invalida! Digite um numero entre",
              minimo, "e", maximo, ".")

        
def verificar_vitoria(tabuleiro, simbolo):
    tamanho = len(tabuleiro)

    # Verifica as linhas
    for i in range(tamanho):
        venceu = True

        for j in range(tamanho):
            if tabuleiro[i][j] != simbolo:
                venceu = False

        if venceu:
            return True

    # Verifica as colunas
    for j in range(tamanho):
        venceu = True

        for i in range(tamanho):
            if tabuleiro[i][j] != simbolo:
                venceu = False

        if venceu:
            return True

    venceu = True

    for i in range(tamanho):
        if tabuleiro[i][i] != simbolo:
            venceu = False

    if venceu:
        return True

    
    venceu = True

    for i in range(tamanho):
        if tabuleiro[i][tamanho - 1 - i] != simbolo:
            venceu = False

    if venceu:
        return True

    return False

