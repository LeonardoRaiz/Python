"""
Exercício 3: Manipulação de Tuplas
Dada uma tupla com elementos (100, 200, 300, 400, 500), escreva um programa que:

Imprime o segundo e o quarto elemento usando indexação.
Tenta modificar o terceiro elemento e captura o erro gerado, imprimindo uma mensagem explicativa.
"""

tupla = (100, 200, 300, 400, 500)
print(f"Segundo elemento: {tupla[1]}")
print(f"Quarto elemento: {tupla[3]}")
try:
    tupla[2] = 600  # Tentativa de modificação
except TypeError as e:
    print("Erro:", e)
