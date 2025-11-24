while True:
    numero = int(input("Digite um número entre 1 e 100: "))

    if numero >= 1 and numero <= 100:
        break   

    print("Valor inválido! Tente novamente.")

print("Número válido inserido:", numero)