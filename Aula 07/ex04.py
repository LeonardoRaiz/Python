"""
Exercício 4: Pedindo Senha
Crie um programa que define uma senha correta (por exemplo, "senha123"). O programa deve pedir ao usuário para digitar a senha repetidamente até que ele acerte. Use um loop while com um contador para limitar as tentativas a cinco. Se o usuário não acertar a senha dentro das tentativas permitidas, use a cláusula else do while para imprimir uma mensagem de bloqueio.
"""

senha_correta = "senha123"
tentativas = 0

while tentativas < 5:
    senha_digitada = input("Digite sua senha: ")
    if senha_digitada == senha_correta:
        print("Senha correta!")
        break
    tentativas += 1
else:
    print("Número de tentativas excedido. Acesso bloqueado.")
