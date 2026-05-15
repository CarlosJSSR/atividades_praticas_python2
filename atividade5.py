'''
Atividade 5 — Par ou Ímpar
Objetivo: Praticar operadores relacionais e módulo (%).
● Enunciado:
13. Solicite um número inteiro;
14. Informe se o número é par ou ímpar.
Desafio extra: Dica: utilize numero % 2.
'''
print("-- Operadores Relacionais e Módulo --")
num = int(input("Digite um número: "))
if num % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")
