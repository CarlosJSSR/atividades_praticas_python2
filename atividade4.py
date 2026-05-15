'''
Atividade 4 — Verificador de Idade
Objetivo: Introdução ao if e else.
● Enunciado:
11. Solicite a idade do usuário;
12. Informe se ele é maior ou menor de idade.
Desafio extra: Desafio extra: se idade >= 60, mostrar 'Idoso'.
'''
print("-- Verificador de Idade --")
idade = int(input("Digite a sua idade "))

if idade >= 18 and idade < 60:
    print("Você é maior de idade")
elif idade < 18:
    print("Você é menor de idade")
elif idade >= 60:
    print("Você é idoso")
else: 
    print("Digite uma idade válida!")
