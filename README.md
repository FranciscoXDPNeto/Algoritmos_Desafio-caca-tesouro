Desafio de programação em python, proposto na matéria de Algoritmos do curso de Engenharia de Softwera da Univassouras.

*Parte 1:*
Exercício de Programação – Jogo de Caça ao
Tesouro
Objetivo
Desenvolver um programa em Python que simule um jogo de caça ao tesouro utilizando matrizes
(listas bidimensionais). O objetivo é praticar conceitos de listas, loops, entrada de dados e
condicionais, implementando um jogo funcional que interaja com o usuário pelo terminal.
Descrição do Problema
Você deverá criar um programa que:
1. Crie um tabuleiro representado por uma matriz 5x5.
2. Posicione um tesouro em uma posição aleatória do tabuleiro.
3. Permita que o jogador faça 7 tentativas para encontrar o tesouro.
4. Para cada tentativa, o jogador deve informar:
o Linha (0 a 4)
o Coluna (0 a 4)
5. Caso o jogador acerte a posição do tesouro:
o Marque a posição no tabuleiro com "T".
o Exiba uma mensagem de vitória e finalize o jogo.
6. Caso o jogador erre:
o Marque a posição escolhida com "X".
o Informe uma dica indicando se o tesouro está mais para cima, baixo, esquerda ou
direita.
7. Ao final das tentativas, caso o tesouro não seja encontrado, exiba a posição correta.
8. Exiba o tabuleiro atualizado após cada tentativa.
Regras e Restrições
• Use listas bidimensionais para representar o tabuleiro.
• O programa deve rodar no terminal; não utilize bibliotecas gráficas.
• As posições do tabuleiro são numeradas de 0 a 4 para linhas e colunas.
• Não permita que o jogador insira valores fora do tabuleiro.
• Evite qualquer comportamento que quebre a execução do programa (como entradas
inválidas).
Exemplo de Execução
=== Tabuleiro ===
~ ~ ~ ~ ~
~ ~ ~ ~ ~
~ ~ ~ ~ ~
~ ~ ~ ~ ~
~ ~ ~ ~ ~
Tentativa 1 de 7
Escolha a linha (0-4): 2
Escolha a coluna (0-4): 3
O tesouro está mais para baixo e mais para a esquerda.
=== Tabuleiro ===
~ ~ ~ ~ ~
~ ~ ~ ~ ~
~ ~ ~ X ~
~ ~ ~ ~ ~
~ ~ ~ ~ ~
Avaliação
• Implementação correta do tabuleiro e matrizes: 3 pontos
• Registro correto das tentativas e marcações: 2 pontos
• Dicas fornecidas corretamente: 2 pontos
• Tratamento de entradas inválidas: 1 ponto
• Código legível e organizado: 2 pontos
Total: 10 pontos

*Parte 2:*
Enunciado – Jogo Campo Minado em Python
Objetivo
Desenvolver um jogo simples de Campo Minado (Minesweeper) em Python, utilizando
matrizes (listas bidimensionais) e funções para organizar o código.
Descrição do Problema
Você deverá implementar uma versão simplificada do Campo Minado em modo texto.
O tabuleiro é representado por uma matriz, onde algumas posições contêm minas e as demais
são espaços seguros.
O jogador deve escolher coordenadas (linha e coluna) e tentar abrir as posições sem explodir
uma mina.
Regras do Jogo
1. O jogo começa com um tabuleiro oculto (exemplo: 5x5).
2. As minas são distribuídas aleatoriamente no tabuleiro.
3. O jogador escolhe posições digitando linha e coluna.
4. Se o jogador abrir:
o Uma célula sem mina, ela mostra quantas minas há nas 8 posições vizinhas.
o Uma célula com mina, o jogo termina ( Game Over).
5. O jogo termina quando:
o O jogador abre todas as células seguras ( Vitória), ou
o Explode uma mina ( Derrota).
Requisitos Técnicos
• O tabuleiro deve ser representado por uma matriz (lista de listas).
• Devem ser usadas funções para modularizar o código, por exemplo:
o criar_tabuleiro(linhas, colunas, qtd_minas)
o mostrar_tabuleiro(tabuleiro, revelado)
o contar_minas_vizinhas(tabuleiro, linha, coluna)
o jogar(tabuleiro)
• Use o módulo random para posicionar minas aleatoriamente.
• Utilize try/except para tratar erros de entrada (ex: coordenadas inválidas).
• O jogador deve ver o progresso a cada jogada.
