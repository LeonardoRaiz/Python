"""
Exercício 2: Encontre o Espaço
Escreva um programa que pede ao usuário para digitar uma frase. Use um loop while para percorrer a frase e imprimir cada caractere até que encontre um espaço. Se nenhum espaço for encontrado, o loop else deve imprimir "Nenhum espaço encontrado na frase."
"""

frase = input("Digite uma frase: ")
i = 0
while i < len(frase):
    if frase[i] == ' ':
        print("Espaço encontrado na posição:", i)
        break
    print(frase[i])
    i += 1
else:
    print("Nenhum espaço encontrado na frase.")
