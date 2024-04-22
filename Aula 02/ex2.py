"""
Exercício 2: IMC
Escreva um programa em Python que calcule o Índice de Massa Corporal (IMC) de uma pessoa utilizando o nome, altura e peso fornecidos. O programa deve imprimir a informação formatada usando f-strings para exibir a altura com duas casas decimais e o IMC também com duas casas decimais.
"""



nome = 'Léo Raiz'
altura = 1.93
peso = 105
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
