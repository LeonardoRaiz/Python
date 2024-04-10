"""
Solicite ao usuário para digitar uma palavra e um caractere. Utilize o operador in para verificar se o caractere está presente na palavra. Se estiver, imprima "{caractere} encontrado em {palavra}". Caso contrário, imprima "{caractere} não encontrado em {palavra}".
"""

palavra = input('Digite uma palavra: ')
caractere = input('Digite um caractere: ')

if caractere in palavra:
    print(f'{caractere} encontrado em {palavra}.')
else:
    print(f'{caractere} não encontrado em {palavra}.')
