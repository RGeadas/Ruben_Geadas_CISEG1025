# Exercício 8: Calcular a Média de 10 Notas e informar notas iguais ou acima da média

notas = [] 

for i in range(1, 11):
    nota = float(input(f"Introduza a nota do aluno {i}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

acima_media = 0
for nota in notas:
    if nota >= media:
        acima_media += 1

print("\n--- Resultados ---")
print(f"Média da turma: {media:.2f}")
print(f"Número de alunos com nota igual ou acima da média: {acima_media}")