"""
Exercício 6: Navegação em Lista de Listas
Considere a lista de listas salas, onde cada sublista contém nomes de alunos de uma sala específica. Escreva um programa que:

Imprime o nome do primeiro aluno de cada sala.
Imprime todos os alunos de cada sala em um formato amigável, como "Alunos na sala 1: Maria, Helena."
"""

salas = [
    ['Maria', 'Helena'],  # Sala 1
    ['Elaine'],           # Sala 2
    ['Luiz', 'João', 'Eduarda']  # Sala 3
]

# Imprimindo o primeiro aluno de cada sala
for indice, sala in enumerate(salas):
    print(f"Primeiro aluno na sala {indice + 1}: {sala[0]}")

# Imprimindo todos os alunos de cada sala
for indice, sala in enumerate(salas):
    alunos = ', '.join(sala)
    print(f"Alunos na sala {indice + 1}: {alunos}")
