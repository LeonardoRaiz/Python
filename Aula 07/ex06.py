"""
Exercício 6: Números Pares com Interrupção
Escreva um programa que usa um loop for para imprimir todos os números pares de 1 a 100. Utilize a cláusula continue para pular números ímpares. Se o loop chegar ao número 50, utilize break para interromper o loop. Use a cláusula else para imprimir uma mensagem dizendo "Loop concluído com sucesso" apenas se o loop não for interrompido prematuramente.
"""

for i in range(1, 101):
    if i == 50:
        print(i)  # Print the number 50 before breaking
        break
    if i % 2 == 0:
        print(i)
    else:
        continue
else:
    print("Loop concluído com sucesso")
