"""
Exercício 4: Nested Loops e Matrizes
Escreva um programa que usa dois loops while aninhados para imprimir uma matriz de 3x3. Cada posição na matriz deve ser representada por um par de coordenadas (linha, coluna). O programa deve imprimir todas as posições da matriz.
"""

linha = 1
qtd_linhas = 3
qtd_colunas = 3

while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'(linha={linha}, coluna={coluna})')
        coluna += 1
    linha += 1
