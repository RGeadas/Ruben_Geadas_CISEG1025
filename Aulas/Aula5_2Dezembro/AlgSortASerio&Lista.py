numeros=[2,5,3,1,9]
#index   0,1,2,3,4
opc=""
i=0

while True:
    print("1 - Ordenar")
    print("2 - Lista")
    print("3 - Sair")
    opc=input("Introduza Opçao: ")
    match opc:
        case "1":
            i=0
            while i<len(numeros):
                if numeros[i]

        case "2":
            for numero in numeros:
                print("numero: ", numero)
        case "3":
            print("Bye Bye")
            break