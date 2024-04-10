"""
Desenvolva um programa que pede ao usuário para inserir uma nota (0 a 100). O programa deve imprimir o grau correspondente à nota de acordo com as seguintes regras:

90 a 100: A
80 a 89: B
70 a 79: C
60 a 69: D
Abaixo de 60: F
"""

nota = int(input('Digite sua nota (0 a 100): '))

if 90 <= nota <= 100:
    print('A')
elif 80 <= nota < 90:
    print('B')
elif 70 <= nota < 80:
    print('C')
elif 60 <= nota < 70:
    print('D')
elif 0 <= nota < 60:
    print('F')
else:
    print('Nota inválida.')
