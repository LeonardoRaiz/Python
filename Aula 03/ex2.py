"""
Escreva um programa que solicita ao usuário que escolha entre três caminhos: esquerda, direita ou frente. Utilize a estrutura if/elif/else para imprimir uma descrição do que o usuário encontra em cada caminho. Por exemplo, se escolher esquerda, pode encontrar um lago; direita, uma floresta; e frente, uma montanha.
"""

caminho = input('Escolha um caminho: esquerda, direita ou frente: ')

if caminho == 'esquerda':
    print('Você encontrou um lago. É um bom lugar para descansar.')
elif caminho == 'direita':
    print('Você entrou em uma floresta escura. Cuidado com os animais selvagens!')
elif caminho == 'frente':
    print('Você vê uma montanha imponente à sua frente. Uma aventura o aguarda!')
else:
    print('Você não escolheu um caminho válido.')
