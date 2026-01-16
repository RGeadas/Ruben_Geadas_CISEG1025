# Exercício 1: Converter Segundos em Horas, Minutos e Segundos

segundos = int(input("Introduza o total de segundos: "))

horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
segundos_restantes = resto % 60

print(f"{horas} hora(s), {minutos} minuto(s) e {segundos_restantes} segundo(s).")
