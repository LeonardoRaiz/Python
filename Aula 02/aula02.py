"""
Variáveis são usadas para salvar algo na memória do computador
PEP8: inicie variáveis com letras minúsculas, pode usar números e undeline _.
O sinal de = é o operador de atribuição. ele é usado para atribuir um valor
a um nome (variável)
USO: nome_variavel = expressão
"""
nome_completo = 'Leonardo Henrique Raiz'
print(nome_completo)
soma_dois_mais_dois = 2 + 2
print(soma_dois_mais_dois)

int_um = int('1')
print(int_um, type(int_um))


nome = "Leonardo"
idade = 34
maior_de_idade = idade >= 18
print("Nome: ", nome, "Idade: ", idade, sep="--")
print("Maior de idade? ", maior_de_idade)


"""
Usando o prompt para inserir informações
"""

numero = input("Digite o valor: ")
print(numero, type(numero))
# F-strings
print(f"Soma do número {numero} + 3 = {int(numero) + 3}")

# -----------------------------------------------------------

concatenacao = 'Leonardo' + ' ' + 'Raiz'
print(concatenacao)

a_dez_vezes = 'A' * 10
tres_vezes_leo = 3 * 'Leo'
print(a_dez_vezes)
print(tres_vezes_leo)

# ---------------------- Precedência entre os operadores --------------------------

#1. (n + n)
#2. **
#3. * / // %
#4. + -

# conta_1 = 1 + 1 ** 5 + 5 # resultado 7
conta_1 = (1 + 1) ** (5 + 5)
print(conta_1)
