# Exercício 6: Desconto de Compra

nome = input("Introduza o nome do cliente: ")
compra = float(input("Introduza o valor da compra (€): "))

if compra <= 200:
    desconto_percent = 10
elif compra <= 500:
    desconto_percent = 15
else:
    desconto_percent = 20

desconto_valor = compra * (desconto_percent / 100)
total = compra - desconto_valor

print("\n--- Recibo de Desconto ---")
print(f"Nome: {nome}")
print(f"Compra: {compra:.2f}€")
print(f"Desconto: {desconto_valor:.2f}€ ({desconto_percent}%)")
print(f"Total a pagar: {total:.2f}€")