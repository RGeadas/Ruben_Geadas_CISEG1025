# organização de codigo, reutilização de codigo, mais efectivo na resolução
num1=2
num2=4
lista1=[1,2,3] 
lista2=[1,2,9] 

def menu ():
    print("1 - Insere")
    print("2 - Proc")
    print("3 - Ordena")
    print("4 - Lista")
    print("5 - Sair")

menu()

# retorno de uma função

def listar (lista): #scope limitado passados por referencia de memoria
    for lis in lista:
        print(lis)

listar(lista1)
listar(lista2)