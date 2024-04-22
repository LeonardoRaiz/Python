"""
Exercício 2: Uso do Loop while
Crie um programa que pede ao usuário para digitar números continuamente até que o número 0 seja digitado. Use um loop while para continuar pedindo os números. Quando 0 for digitado, o loop deve terminar e o programa deve imprimir "Loop encerrado".
"""

print("Digite números e digite 0 para sair.")
while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        print("Loop encerrado")
        break
