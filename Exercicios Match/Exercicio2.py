"""2. Classificação de nota
Lê uma nota (0–100) e retorna uma classificação:
•	90 ou mais → Excelente
•	70–89 → Bom
•	50–69 → Suficiente
•	Abaixo de 50 → Insuficiente
Exemplo:
Entrada → Bom
Saída →  70-89
"""

nota = int(input("Digite a nota (0–100) "))

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Bom")
elif nota >= 50:
    print("Suficiente")
else:
    print("Insuficiente")
