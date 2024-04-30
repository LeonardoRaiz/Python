"""
Exercício 2: Empacotamento e Desempacotamento de Listas
Crie uma lista com cinco nomes. Utilize empacotamento e desempacotamento para atribuir o primeiro nome a uma variável, os próximos três nomes a outra variável e o último nome a uma terceira variável. Imprima todas as variáveis para verificar se a atribuição foi realizada corretamente.
"""

nomes = ['Ana', 'Bruno', 'Carla', 'David', 'Eva']
primeiro, *meio, ultimo = nomes
print(f"Primeiro: {primeiro}")
print(f"Meio: {meio}")
print(f"Último: {ultimo}")
