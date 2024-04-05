# Isso é um comentário!

print(123)

"""
DocString como comentários
Aqui pode escrever quantas linhas necessárias
"""

print("Hello World")


# --------------------------------------------------------------

#Usando separador (separar os argumentos) e end (encerramento do print)
print(12, 34, sep="-", end='##')
print(11, 55, sep="-")
print(56, 78, sep='--')

# -------------------- Tipos de Dados --------------------------------------

"""
Python = Linguagem de programação
Tipo de tipagem = Dinâmica / Forte
str -> string -> texto
Strings são textos que estão dentro de aspas
"""

# Aspas simples
print('Leonardo Raiz')

# Aspas duplas
print("Leonardo Raiz")

# Escape
print("Leonardo \"Raiz\"")
print("Forma mais clara -", 'Leonardo "Raiz"')

# r
print(r"Leonardo \"Raiz\"")

# ---------------------------------------------------------------------------------

"""
Tipos int e float
int -> Número inteiro
O tipo int representa qualquer número positivo ou negativo.
int sem sinal é considerado positivo
"""

print(10)  # int
print(-10) # int
print(0) # int números literais


"""
Tipos int e float
float -> Número com ponto flutuante
O tipo int representa qualquer número positivo ou negativo com ponto flutuante.
float sem sinal é considerado positivo
"""
print(1.10) # float

# A função ou classe! type mostra o tipo que o Python inferiu o valor

print( type(10) )
print( type(10.5) )
print( type('teste') )

# ----------------------------------------------------------------------

"""
Tipo de dado bool (boolean)
Ao questionar algo em um programa, só existem duas respostas possíveis:
SIM (true) ou NÃO (false)
Existem vários operadores para "questionar". Dentre eles o ==, que é um operador lógico
que questiona se um valor é igual a outro
"""
print(10 == 10) #Sim => True (Verdadeiro)
print(10 == 11) #Não => False (Falso)
print(type(10 == 11))

# ---------------------------------------------------------------

"""
Conversão de tipo, coerção 
type convertion, typecasting, coercion
é o ato de converter um tipo em outro
tipos imutáveis e primitivos:
int, float, str, bool
"""

print(1 + 1)
print('a' + 'b')
# print("1" + 1) # Funciona ?
print(int('1'), type(int('1')))
print(int("1") + 1)
print(str(11) + 'b')
print(bool(' '))


