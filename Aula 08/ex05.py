"""
Exercício 5: Clonando e Modificando Listas
Dada uma lista de elementos, clone esta lista e faça uma alteração em qualquer elemento da lista original. Imprima ambas as listas para mostrar que a lista clonada não foi modificada. Utilize o método copy para a clonagem.
"""

lista_original = ['a', 'b', 'c', 'd', 'e']
lista_clonada = lista_original.copy()

# Modificando um elemento da lista original
lista_original[2] = 'x'

# Imprimindo ambas as listas
print("Lista Original:", lista_original)
print("Lista Clonada:", lista_clonada)
