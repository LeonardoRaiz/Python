"""
Exercício 3: Alterando e Deletando Elementos
Crie uma lista com cinco números (ex: [5, 10, 15, 20, 25]). Faça o seguinte:

Modifique o terceiro elemento para ser o dobro do seu valor original.
Delete o segundo elemento da lista.
Imprima o elemento que agora ocupa a posição do elemento deletado.
Imprima a lista final.

"""
lista = [5, 10, 15, 20, 25]

# Modificando o terceiro elemento para ser o dobro do valor original
lista[2] *= 2

# Deletando o segundo elemento da lista
item_deletado = lista.pop(1)
print("Item deletado:", item_deletado)

# Imprimindo o elemento que agora ocupa a posição do elemento deletado
print("Novo segundo elemento:", lista[1])

# Imprimindo a lista final
print("Lista final:", lista)
