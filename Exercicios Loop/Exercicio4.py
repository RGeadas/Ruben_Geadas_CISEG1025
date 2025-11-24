numero = int(input("Digite um número inteiro: "))

if numero <= 1:
    print("O número não é primo.")
else:
    divisores = 0
    contador = 1

    while contador <= numero:
        if numero % contador == 0:
            divisores = divisores + 1

        contador = contador + 1  

    if divisores == 2:
        print("O número é primo.")
    else:
        print("O número não é primo.")