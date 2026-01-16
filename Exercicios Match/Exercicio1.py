#1. Tipo de dia
#Cria um programa que receba o nome de um dia da semana e diga se é dia útil ou fim de semana.
#Exemplo:
#Entrada → domingo
#Saída → Fim de semana

dia = input("Digite o dia da semana ").lower()

if dia in ["sábado", "sabado", "domingo"]:
    print("Fim de semana")
elif dia in ["segunda", "terça", "terca", "quarta", "quinta", "sexta"]:
    print("Dia útil")
else:
    print("Dia inválido")
