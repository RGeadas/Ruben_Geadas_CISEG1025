print("Veja se o numero é Par ou Impar")

for i in range(10):
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        print("O número", numero, "é Par")
    else:
        print("O número", numero, "é Impar")