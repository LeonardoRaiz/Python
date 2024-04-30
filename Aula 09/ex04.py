"""
Exercício 4: Enumerando Elementos
Dada uma lista de frutas ['Maçã', 'Banana', 'Cereja'], use o loop for com enumerate para imprimir cada fruta e seu respectivo índice em formato de lista, por exemplo: 1 - Banana.
"""

frutas = ['Maçã', 'Banana', 'Cereja']
for indice, fruta in enumerate(frutas):
    print(f"{indice + 1} - {fruta}")
