"""
Exercício 2: Adicionando e Removendo Elementos
Escreva um programa que começa com uma lista vazia e realiza as seguintes operações:

Peça ao usuário para adicionar três itens à lista usando o método append.
Remova o último item inserido usando o método pop e imprima o item removido.
Peça ao usuário um índice e um valor para inserir na lista usando o método insert.
Imprima a lista final.
"""

lista = []

# Adicionando três itens à lista
for _ in range(3):
    item = input("Digite um item para adicionar à lista: ")
    lista.append(item)

# Removendo o último item inserido e imprimindo
ultimo_item = lista.pop()
print("Item removido:", ultimo_item)

# Inserindo um novo item em um índice específico
indice = int(input("Digite o índice para inserir um novo item: "))
novo_item = input("Digite o novo item: ")
lista.insert(indice, novo_item)

# Imprimindo a lista final
print("Lista final:", lista)
