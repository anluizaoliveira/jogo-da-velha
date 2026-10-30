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

    
    for i in range(tamanho):
        venceu = True

        for j in range(tamanho):
            if tabuleiro[i][j] != simbolo:
                venceu = False

        if venceu:
            return True


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

def contar_vazias(tabuleiro, tamanho):
    vazias = 0

    for i in range(tamanho):
        for j in range(tamanho):
            if tabuleiro[i][j] == " ":
                vazias = vazias + 1

    return vazias

def mostrar_regras():
    print("\n===== REGRAS DO JOGO =====")
    print("Dois jogadores participam: X e O.")
    print("O jogador X comeca.")
    print("Cada jogador escolhe uma linha e uma coluna.")
    print("As linhas e colunas vao de 1 a 3.")
    print("Vence quem alinhar tres simbolos iguais.")
    print("O alinhamento pode ser horizontal, vertical")
    print("ou diagonal.")
    print("Se nao houver casas vazias e ninguem vencer,")
    print("a partida termina empatada.")
    print("==========================\n")

