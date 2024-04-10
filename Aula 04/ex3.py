"""
Escreva um programa que solicita ao usuário um número flutuante representando um valor monetário. Utilize a formatação básica de strings para imprimir esse valor com duas casas decimais e um sinal de "+" caso o valor seja positivo. Por exemplo, um input de 1234.5 deve resultar em "+1234.50".
"""

valor = float(input("Digite um valor monetário: "))
print(f"{valor:0>+1.2f}")
