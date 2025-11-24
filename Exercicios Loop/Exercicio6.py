contador = 0    
nPrimo = 2       

while contador < 10:
    i = 1
    divisores = 0

    while i <= nPrimo:
        if nPrimo % i == 0:
            divisores = divisores + 1
        i = i + 1

    if divisores == 2:
        print(nPrimo)
        contador = contador + 1

    nPrimo = nPrimo + 1  