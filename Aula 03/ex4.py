"""
Crie um programa que define uma senha senha_secreta (por exemplo, "python123"). Em seguida, ele pede ao usuário para digitar uma senha. Se a senha estiver correta, imprima "Acesso concedido". Se a senha estiver incorreta, imprima "Acesso negado".
"""

senha_secreta = 'python123'
senha = input('Digite a senha: ')

if senha == senha_secreta:
    print('Acesso concedido')
else:
    print('Acesso negado')
