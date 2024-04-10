"""
Solicite ao usuário para inserir uma frase. Primeiro, imprima a frase ao contrário. Em seguida, peça ao usuário para fornecer dois números: um índice inicial e um índice final. Imprima a substring que começa no índice inicial e termina no índice final da frase original.
"""

frase = input("Digite uma frase: ")
print(f"A frase ao contrário é: {frase[::-1]}")

indice_inicial = int(input("Digite o índice inicial: "))
indice_final = int(input("Digite o índice final: "))
print(f"A substring é: {frase[indice_inicial:indice_final]}")
