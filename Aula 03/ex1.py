"""
Compara os dois valores inseridos pelo usuário. Se o primeiro_valor for maior ou igual ao segundo_valor, o programa deve imprimir uma mensagem formatada que indica que o primeiro_valor é maior ou igual ao segundo_valor.
Se o primeiro_valor for menor que o segundo_valor, o programa deve imprimir uma mensagem formatada indicando que o segundo_valor é maior do que o primeiro_valor.
"""

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )