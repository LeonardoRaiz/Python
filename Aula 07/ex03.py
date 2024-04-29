"""
Exercício 3: Contagem de Caracteres
Solicite ao usuário para inserir uma palavra. Use um loop while para determinar qual caractere aparece mais vezes na palavra. Imprima o caractere e a quantidade de vezes que ele aparece. Se a palavra for composta apenas por um único caractere repetido, imprima uma mensagem especial indicando isso.
"""

palavra = input("Digite uma palavra: ")
i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(palavra):
    letra_atual = palavra[i]
    qtd_atual = palavra.count(letra_atual)
    if qtd_atual > qtd_apareceu_mais_vezes:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual
    i += 1

if qtd_apareceu_mais_vezes == len(palavra):
    print(f'Todos os caracteres são iguais: "{letra_apareceu_mais_vezes}" apareceu {qtd_apareceu_mais_vezes} vezes.')
else:
    print(f'A letra que apareceu mais vezes foi "{letra_apareceu_mais_vezes}", que apareceu {qtd_apareceu_mais_vezes} vezes.')
