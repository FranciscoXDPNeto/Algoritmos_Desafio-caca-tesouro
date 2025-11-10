import random

def criar_tabuleiro(linhas, colunas, qtd_minas):
    tabuleiro = [["." for _ in range(colunas)] for _ in range(linhas)]
    minas = 0

    while minas < qtd_minas:
        l = random.randint(0, linhas - 1)
        c = random.randint(0, colunas - 1)
        if tabuleiro[l][c] != "*":
            tabuleiro[l][c] = "*"
            minas += 1

    return tabuleiro

def contar_minas_vizinhas(tabuleiro, linha, coluna):
    direcoes = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0),  (1, 1)
    ]
    linhas = len(tabuleiro)
    colunas = len(tabuleiro[0])
    contador = 0

    for dl, dc in direcoes:
        nl = linha + dl
        nc = coluna + dc
        if 0 <= nl < linhas and 0 <= nc < colunas:
            if tabuleiro[nl][nc] == "*":
                contador += 1

    return contador

def mostrar_tabuleiro(tabuleiro, revelado):
    print("\n=== TABULEIRO ===")
    for i in range(len(tabuleiro)):
        linha_exibida = []
        for j in range(len(tabuleiro[0])):
            if revelado[i][j]:
                if tabuleiro[i][j] == "*":
                    linha_exibida.append("*")
                else:
                    qtd = contar_minas_vizinhas(tabuleiro, i, j)
                    linha_exibida.append(str(qtd))
            else:
                linha_exibida.append("#")
        print(" ".join(linha_exibida))
    print()

def ler_posicao(linhas, colunas):
    while True:
        try:
            l = int(input("Linha: "))
            c = int(input("Coluna: "))
            if 0 <= l < linhas and 0 <= c < colunas:
                return l, c
            else:
                print("Coordenadas inválidas! Digite valores dentro do tabuleiro.")
        except ValueError:
            print("Entrada inválida! Digite números inteiros.")

def jogar():
    linhas = 5
    colunas = 5
    qtd_minas = 5

    tabuleiro = criar_tabuleiro(linhas, colunas, qtd_minas)
    revelado = [[False for _ in range(colunas)] for _ in range(linhas)]

    celulas_seguras = linhas * colunas - qtd_minas
    abertas = 0

    print("=== CAMPO MINADO ===")
    mostrar_tabuleiro(tabuleiro, revelado)

    while True:
        print("Escolha uma posição para revelar:")
        linha, coluna = ler_posicao(linhas, colunas)

        if revelado[linha][coluna]:
            print("Você já abriu esta posição!")
            continue

        revelado[linha][coluna] = True

        if tabuleiro[linha][coluna] == "*":
            mostrar_tabuleiro(tabuleiro, [[True]*colunas for _ in range(linhas)])
            print("BOOM! Você encontrou uma mina! Fim de jogo.")
            break

        abertas += 1

        mostrar_tabuleiro(tabuleiro, revelado)

        if abertas == celulas_seguras:
            print("PARABÉNS! Você venceu! Todas as células seguras foram abertas.")
            break

jogar()