'''
Atividade 7 — Mini Sistema de Login
Objetivo: Introdução à comparação de dados.
● Enunciado:
17. Peça usuário e senha;
18. Verifique se usuário = admin e senha = 1234.
Saída esperada:
Acesso permitido
ou
Usuário ou senha incorretos
'''
print("-- Comparação de Dados --")
usuario = input("Digite o seu nome de usuário: ")
senha = input("Digite a sua senha: ")
if senha == "1234" and usuario == "admin":
    print(f"Acesso Permitido!\nBem-vindo(a) {usuario}!")
else:
    print("Acesso Negado!\nUsuário e/ou senha incorretos!")
