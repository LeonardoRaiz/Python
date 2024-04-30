"""
Exercício 4: Dividindo e Unindo Strings
Peça ao usuário para inserir uma frase longa. Use o método split para dividir a frase em palavras, remova os espaços em branco extras e, em seguida, use o método join para reconstruir a frase com as palavras separadas por um único espaço. Imprima a frase original e a frase processada para comparação.
"""

frase = input("Digite uma frase longa: ")
palavras = frase.split()
frase_reconstruida = ' '.join(palavras)
print("Frase original:", frase)
print("Frase processada:", frase_reconstruida)
