"""5. Análise de mensagem
Recebe uma mensagem e retorna:
•	“Saudação” se for “olá” ou “bom dia”
•	“Pergunta” se terminar com “?”
•	“Despedida” se contiver “tchau” ou “adeus”
•	“Mensagem genérica” caso contrário
Exemplo:
Entrada → “Tudo bem?”
Saída → Pergunta
"""

mensagem = input("Digite uma mensagem ").lower()

if mensagem in ["olá", "ola", "bom dia"]:
    print("Saudação")
elif mensagem.endswith("?"):
    print("Pergunta")
elif "tchau" in mensagem or "adeus" in mensagem:
    print("Despedida")
else:
    print("Mensagem genérica")
