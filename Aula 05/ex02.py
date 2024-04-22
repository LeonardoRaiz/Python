"""
Exercício 2: Divisão Segura
Peça ao usuário para digitar dois números. Use um bloco try/except para lidar com a divisão dos números. Se a divisão for possível, imprima o resultado. Se a divisão por zero ocorrer, imprima "Erro: divisão por zero".
"""

num1 = input("Digite o numerador: ")
num2 = input("Digite o denominador: ")

try:
    num1 = float(num1)
    num2 = float(num2)
    resultado = num1 / num2
    print(f"O resultado da divisão é {resultado:.2f}")
except ValueError:
    print("Por favor, insira apenas números.")
except ZeroDivisionError:
    print("Erro: divisão por zero.")
