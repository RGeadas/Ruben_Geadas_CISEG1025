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

status = input("Status (ok/erro) ").lower()
tempo = int(input("Tempo de resposta (ms) "))

servidor = {"status": status, "tempo_resposta": tempo}

if servidor["status"] == "ok" and servidor["tempo_resposta"] > 200:
    print("Servidor lento")
elif servidor["status"] == "ok":
    print("Servidor ativo")
elif servidor["status"] == "erro":
    print("Servidor indisponível")
else:
    print("Estado desconhecido")
