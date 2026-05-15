'''
Atividade 1 — Cadastro Simples
Objetivo: Praticar entrada e saída de dados.
● Enunciado:
1. Peça o nome do usuário;
2. Peça a idade;
3. Peça o curso;
4. Exiba uma mensagem formatada com as informações.
Exemplo de entrada:
Digite seu nome: Ana
Digite sua idade: 20
Digite seu curso: Ciência da Computação
Saída esperada:
Olá Ana!
Você tem 20 anos e cursa Ciência da Computação.
'''
print("-- Sistema de Cadastro --")
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
curso = input("Digite seu curso: ")

print(f"Olá {nome}!\nVocê tem {idade} anos e cursa {curso}")
