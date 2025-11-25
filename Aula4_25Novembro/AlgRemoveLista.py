marcas=["BMW","Fiat", "Tesla", "Ford"]
modelos=["M3", "Panda", "Model 3", "CAPRI"]
#indice   0       1        2          3
opc=""
removeIndice=0

while True:
    print("1 - Remover")
    print("2 - Listar")
    print ("3 - Sair")
    opc=input("Introduza opcão")
    match opc:
        case "1":
            removeIndice=int(input("Introduza indice do carro para remover"))
            marcas.pop(removeIndice)
            modelos.pop(removeIndice)
        case "2":
            print("Stand AUTO")
            for i in range(len(marcas)):
                print("indice ", i , " ", marcas[i],"  ",modelos[i])
        case "3":
            print("Sair do programa")
            break
        case _:
            print("Opção Errada")