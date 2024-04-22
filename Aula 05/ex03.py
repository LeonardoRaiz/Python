"""
 Escreva um programa em Python que calcule o fatorial de um número inteiro fornecido pelo usuário. O programa deve garantir que o número seja um inteiro e não um float ou qualquer outro tipo não inteiro.
"""
import math

numero_str = input("Digite um número inteiro para calcular o fatorial: ")
try:
    # Tenta converter a entrada para um inteiro
    numero = int(numero_str)

    # Verifica se a string original é igual à sua versão inteira
    # Isso é para garantir que entradas como '5.0' sejam rejeitadas
    if str(numero) != numero_str:
        raise ValueError("O número digitado não é um inteiro puro.")

    # Calcula o fatorial usando a função factorial do módulo math
    fatorial = math.factorial(numero)
    print(f"O fatorial de {numero} é {fatorial}.")
except ValueError as e:
    print(f"Erro: {e}\nPor favor, digite um número inteiro.")