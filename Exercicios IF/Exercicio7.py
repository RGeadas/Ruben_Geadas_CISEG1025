# Exercício 7: Calcular a Média de Notas com Pesos

nota1 = float(input("Introduza a 1ª nota: "))
nota2 = float(input("Introduza a 2ª nota: "))
nota3 = float(input("Introduza a 3ª nota: "))

peso1 = 2
peso2 = 3
peso3 = 5

media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

if media >= 6:
    resultado = "Aprovado"
else:
    resultado = "Reprovado"

print(f"\nMédia: {media:.1f}")
print(resultado)