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

def mostrar_placar(placar):
    print("\n===== PLACAR =====")
    print("Vitorias de X:", placar["X"])
    print("Vitorias de O:", placar["O"])
    print("Empates:", placar["Empates"])
    print("==================\n")

def jogar_partida(placar, historico, registros):
    tamanho = 3
    tabuleiro = criar_tabuleiro(tamanho)

    # Tuplas identificam os jogadores
    jogador_x = input("Nome do jogador X: ").strip()
    jogador_o = input("Nome do jogador O: ").strip()

    if jogador_x == "":
        jogador_x = "Jogador X"

    if jogador_o == "":
        jogador_o = "Jogador O"

    jogador_x = jogador_x.upper()
    jogador_o = jogador_o.upper()

    jogadores = {
        "X": jogador_x,
        "O": jogador_o
    }


    casas_usadas = set()

    simbolo = "X"
    resultado = ""

    while True:
        mostrar_tabuleiro(tabuleiro, tamanho)

        print("Vez de", jogadores[simbolo], "(" + simbolo + ")")

        linha = ler_numero("Escolha a linha (1 a 3): ", 1, 3) - 1
        coluna = ler_numero("Escolha a coluna (1 a 3): ", 1, 3) - 1

        # Cada posicao e uma tupla (linha, coluna)
        posicao = (linha, coluna)

        if posicao in casas_usadas:
            print("Essa casa ja foi escolhida. Tente novamente.")
            continue

        if tabuleiro[linha][coluna] != " ":
            print("Essa casa esta ocupada. Tente novamente.")
            continue

        tabuleiro[linha][coluna] = simbolo
        casas_usadas.add(posicao)

        if verificar_vitoria(tabuleiro, simbolo):
            mostrar_tabuleiro(tabuleiro, tamanho)

            print("Vitoria de", jogadores[simbolo] + "!")

            placar[simbolo] = placar[simbolo] + 1

            nome_vencedor = jogadores[simbolo]

            if nome_vencedor not in registros:
                registros[nome_vencedor] = 0

            registros[nome_vencedor] = (
                registros[nome_vencedor] + 1
            )

            resultado = nome_vencedor + " venceu"
            break

        if contar_vazias(tabuleiro, tamanho) == 0:
            mostrar_tabuleiro(tabuleiro, tamanho)

            print("A partida terminou empatada!")

            placar["Empates"] = placar["Empates"] + 1
            resultado = "Empate"
            break

        if simbolo == "X":
            simbolo = "O"
        else:
            simbolo = "X"

    
    partida = (jogador_x, jogador_o, resultado)
    historico.append(partida)

    print("Resultado registrado no historico.\n")



def mostrar_historico(historico):
    print("\n===== HISTORICO =====")

    if len(historico) == 0:
        print("Nenhuma partida realizada.")
    else:
        for i in range(len(historico)):
            partida = historico[i]

            print(
                str(i + 1) + ". " +
                partida[0] + " x " +
                partida[1] + " - " +
                partida[2]
            )

    print("=====================\n")

def mostrar_estatisticas(placar, historico):
    total = len(historico)

    print("\n===== ESTATISTICAS =====")
    print("Total de partidas:", total)
    print("Vitorias de X:", placar["X"])
    print("Vitorias de O:", placar["O"])
    print("Empates:", placar["Empates"])

    if total > 0:
        percentual_x = round(placar["X"] * 100 / total, 1)
        percentual_o = round(placar["O"] * 100 / total, 1)
        percentual_empates = round(
            placar["Empates"] * 100 / total, 1
        )

        print("Percentual de vitorias de X:",
              str(percentual_x) + "%")
        print("Percentual de vitorias de O:",
              str(percentual_o) + "%")
        print("Percentual de empates:",
              str(percentual_empates) + "%")

    print("========================\n")

def mostrar_ranking(registros):
    ranking = []

    for nome in registros:
        item = (registros[nome], nome)
        ranking.append(item)

    ranking.sort(reverse=True)

    print("\n===== RANKING =====")

    if len(ranking) == 0:
        print("Ainda nao existem vitorias registradas.")
    else:
        for i in range(len(ranking)):
            print(
                str(i + 1) + "º - " +
                ranking[i][1] + ": " +
                str(ranking[i][0]) + " vitoria(s)"
            )

    print("===================\n")
