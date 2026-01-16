numero=0
lista=[1,2,3]

while True:

    try:
        print(lista[3])
       
    except IndexError as error:
        print("Deu erro", error)
    try:
        numero=int(input("numero"))
    except ValueError as errorv:
        print("deu erro", errorv)
    print(numero)   