'''
Atividade 6 — Conversor de Temperatura
Objetivo: Trabalhar fórmulas matemáticas.
● Enunciado:
15. Solicite uma temperatura em Celsius;
16. Converta para Fahrenheit.
Fórmula:
F = (C × 1.8) + 32
'''
print("-- Fórmulas Matemáticas --")
celsius = float(input("Digite uma temperatura em °C: "))
fahrenheit = (celsius*1.8) + 32
print(f"Temperatura em °F: {fahrenheit}°")
