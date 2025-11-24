i = 0  

while i <= 255:
   
    for x in range(20):
        if i > 255:
            break  

        print(i, "->", chr(i))
        i = i + 1

    print("\nDeseja continuar? (S/N)")
    resposta = input().lower()

    if resposta == "n":
        print("Programa terminado.")
        break
