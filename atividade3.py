'''
Atividade 3 — Média do Aluno
Objetivo: Utilizar variáveis e operadores.
● Enunciado:
7. Peça o nome do aluno;
8. Peça a Nota 1;
9. Peça a Nota 2;
10. Calcule a média e exiba o resultado.
Saída esperada:
Aluno: Carlos
Média: 8.5
'''
print("-- Calcular Média da Nota --")
aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2
print(f"Média: {media:.1f}")
