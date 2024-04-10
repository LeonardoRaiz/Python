"""
Peça ao usuário para inserir uma temperatura em Celsius. Converta esse valor para Fahrenheit usando a fórmula (Celsius * 9/5) + 32. Imprima o resultado com a mensagem "XX°C é igual a YY°F", assegurando que o valor em Fahrenheit seja mostrado com apenas uma casa decimal.
"""

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C é igual a {fahrenheit:.1f}°F")
