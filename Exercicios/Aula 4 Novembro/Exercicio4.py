# Exercício 4: Verificar se o Cheque Pode Ser Descontado

saldo = float(input("Introduza o saldo da conta: "))
cheque = float(input("Introduza o valor do cheque: "))

if cheque <= saldo:
   
    saldo -= cheque  
    print(f"Cheque descontado, saldo: {saldo:.2f}")
else:
    print("O cheque não pode ser descontado (saldo insuficiente).")