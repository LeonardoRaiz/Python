"""
Exercício 5: Operadores de Atribuição em Aplicação Prática
Crie um programa que define uma variável saldo inicializada em 100.0. Em seguida, o programa deve aplicar uma série de operações:

Adicionar 50 ao saldo.
Subtrair 30 do saldo.
Multiplicar o saldo por 1.1 (adicione 10% de bônus).
Dividir o saldo por 2.
Após cada operação, imprima o saldo atualizado.
"""

saldo = 100.0
saldo += 50
print(f"Adicionando 50: {saldo}")
saldo -= 30
print(f"Subtraindo 30: {saldo}")
saldo *= 1.1
print(f"Multiplicando por 1.1: {saldo}")
saldo /= 2
print(f"Dividindo por 2: {saldo}")
