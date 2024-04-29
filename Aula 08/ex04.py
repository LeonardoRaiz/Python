"""
Exercício 4: Concatenação de Listas
Defina duas listas, uma com os três primeiros meses do ano e outra com os três meses seguintes. Concatene as duas listas de duas maneiras:

Usando o operador + e imprima o resultado.
Usando o método extend e imprima a lista modificada.
"""

meses_iniciais = ['Janeiro', 'Fevereiro', 'Março']
meses_finais = ['Abril', 'Maio', 'Junho']

# Concatenando as listas usando o operador +
meses_concatenados = meses_iniciais + meses_finais
print("Concatenação com operador +:", meses_concatenados)

# Usando o método extend para concatenar as listas
meses_iniciais.extend(meses_finais)
print("Concatenação com método extend:", meses_iniciais)
