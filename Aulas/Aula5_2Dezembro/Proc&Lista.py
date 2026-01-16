marcas= ["BMW", "FIAT" , "TESLA"  , "FORD" , "FIAT" ]
modelos=["M3" , "PANDA", "Model 3", "CAPRI", "PANDA"]
anos=   [2001 , 2002   , 2006     , 2012   ,  2021  ]
#indice   0   , 1      , 2        , 3      ,    4
opc=""
valorIntrodProc=""
flagFind=True
flagWhile=True
flagi=0
flagApaga="S"

#valorIntrodProc e marcas[1]
#      FIAT      e   FIAT
#     unicode    e  unicode
     
while flagWhile:
        i=0
        flagFind=True
        print("1 - Remover Marca")
        print("2 - Remover Modelo")
        print("3 - Lista")
        print("4 - Sair")
        opc=input("Introduza opção: ")
        match opc:
                case "1":

                    valorIntrodProc=input("Introduza a Marca para remover: ")
                    controleWhile=len(marcas)
                    while i<controleWhile: 
                        if valorIntrodProc==marcas[i]: #true or false
                            print("Encontrei a marca na posiçao: ", i, "com o nome: ", marcas[i], end="")
                            print(" Modelo: ", modelos[i], " Anos: ", anos[i])
                            flagFind=False
                            flagApaga=input("Quer apagar esta Marca, modelo e ano S/N: ")
                            if flagApaga=="s" or flagApaga=="S":
                                marcas.pop(i)
                                modelos.pop(i)
                                anos.pop(i)
                                controleWhile-=1 
                            i+=1                      
                    if flagFind: #mesmo que flagFind == true
                         print("Nao existe igualdade")

                case "2":
                    valorIntrodProc=input("Introduza o Modelo para procurar: ")
                    while i<len(modelos):
                        if valorIntrodProc == modelos[i]:
                              print("Encontrei a marca na posiçao: ", i, "com o nome: ", marcas[i])
                              flagFind==False 
                    if flagFind: # mesmo que flagFind == true
                            print("Nao existe igualdade") 

                case "3":
                    for i in range(len(marcas)):
                         print("Marca: ", marcas[i], "Modelos: ", modelos[i], "Ano: ", anos[i])
                case "4":
                    print("Adeus e obrigado")
                    flagWhile=False
                    break