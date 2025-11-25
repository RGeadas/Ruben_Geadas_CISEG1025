marcas=[]
modelos=[]
opc=""

while True:
    print("1 - Inserir Marca e Modelo")
    print("2 - Listar")
    print("3 - Sair do Programa")
    opc=input("Introduza uma opção: ")
   
    match opc:
        case "1":
            print("Inserir a Marca e depois o Modelo")
            print("Marca: ")
            marcas.append(input())
            print("Modelo: ")
            modelos.append(input())
        case "2":
            print("Lista Stand") 
            # print("marcas:", marcas, "Modelos " ,modelos)
            print("Numero total: ", len(marcas))
            print("Marcas     Modelos")
            for i in range(len(marcas)):
                print(marcas[i] ,"  ",modelos[i])
        case "3":
            print("A sair do programa")
            break #serve para parar o while True


