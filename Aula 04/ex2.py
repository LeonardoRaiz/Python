"""
Utilize a interpolação básica de strings para criar uma mensagem personalizada. Peça ao usuário para inserir seu nome e sua idade. Em seguida, imprima uma mensagem dizendo "Olá, [nome]! No próximo ano, você terá [idade+1] anos." Use %s para o nome e %d para a idade.
"""

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
mensagem = "Olá, %s! No próximo ano, você terá %d anos." % (nome, idade + 1)
print(mensagem)
