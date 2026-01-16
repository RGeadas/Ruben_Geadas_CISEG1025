# Exercício 3: Mostrar Números em Ordem Crescente e Decrescente (versão manual)

num1 = int(input("Introduza o primeiro número: "))
num2 = int(input("Introduza o segundo número: "))

if num1 < num2:
    print(f"Crescente: {num1}, {num2}")
    print(f"Decrescente: {num2}, {num1}")
else:
    print(f"Crescente: {num2}, {num1}")
    print(f"Decrescente: {num1}, {num2}")