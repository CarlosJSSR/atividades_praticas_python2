'''
Atividade 2 — Calculadora de Soma
Objetivo: Trabalhar operadores matemáticos.
● Enunciado:
5. Solicite dois números inteiros ao usuário;
6. Mostre soma, subtração, multiplicação e divisão.
Desafio extra: Desafio extra: mostrar também o resto da divisão.
'''
print("-- Calculadora de Soma --")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
if num1 != 0 or num2 != 0:
    divisao = num1 / num2
else:
    divisao = "Divisão por 0 não existe!"
modulo = num1 % num2
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Resto da Divisão: {modulo}")
