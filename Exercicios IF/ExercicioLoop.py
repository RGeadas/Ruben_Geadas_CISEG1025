# Exercício Loop: Identificar Números Pares e Ímpares

pares = 0
impares = 0

for i in range(1, 11):
    numero = int(input(f"Introduza o {i}º número: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("\n--- Resultado ---")
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")