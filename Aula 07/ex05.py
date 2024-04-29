"""
Exercício 5: Transformação de Texto com for
Peça ao usuário para digitar uma frase. Use um loop for para adicionar asteriscos antes e depois de cada caractere na frase. Por exemplo, a frase "gato" deve ser transformada em "gato*". Imprima a nova string transformada.
"""

frase = input("Digite uma frase: ")
novo_texto = ''
for letra in frase:
    novo_texto += f'*{letra}'
novo_texto += '*'
print(novo_texto)
