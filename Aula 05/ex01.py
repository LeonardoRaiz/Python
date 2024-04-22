"""
Exercício 1: Conversão de String para Float
Peça ao usuário para inserir um número. Use um bloco try/except para converter a entrada em um número float. Se a conversão for bem-sucedida, imprima o dobro desse número. Se a conversão falhar, imprima "Por favor, insira um número válido".
"""

numero_str = input("Digite um número para dobrar: ")
try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except ValueError:
    print('Por favor, insira um número válido.')
